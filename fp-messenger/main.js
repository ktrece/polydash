import * as THREE from "three";
import { FP_BUILDINGS } from "./data.js";

/* =========================================================================
   FP Messenger · Castilla y León
   Mini-mundo 3D (réplica MVP inspirada en messenger.abeto.co).
   Caminas sobre un planeta esférico; cada casa es una familia de FP.
   Una brújula 3D te persigue y apunta al edificio más cercano.
   ========================================================================= */

const R = 22; // radio del planeta
const canvas = document.getElementById("scene");

/* ---------- Renderer / escena / cámara ---------- */
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);

const scene = new THREE.Scene();
scene.background = new THREE.Color("#0a1330");
scene.fog = new THREE.FogExp2("#0a1330", 0.012);

const camera = new THREE.PerspectiveCamera(
  55,
  window.innerWidth / window.innerHeight,
  0.1,
  500
);

/* ---------- Luces ---------- */
const hemi = new THREE.HemisphereLight("#bcd4ff", "#243056", 0.9);
scene.add(hemi);
const sun = new THREE.DirectionalLight("#fff3da", 1.15);
sun.position.set(40, 60, 30);
scene.add(sun);
scene.add(new THREE.AmbientLight("#445", 0.35));

/* ---------- Estrellas de fondo ---------- */
(function addStars() {
  const g = new THREE.BufferGeometry();
  const n = 600;
  const pos = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    const v = new THREE.Vector3()
      .randomDirection()
      .multiplyScalar(180 + Math.random() * 60);
    pos.set([v.x, v.y, v.z], i * 3);
  }
  g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  scene.add(
    new THREE.Points(
      g,
      new THREE.PointsMaterial({ color: "#cdddff", size: 0.7, sizeAttenuation: true })
    )
  );
})();

/* ---------- Planeta ---------- */
const planet = new THREE.Group();
scene.add(planet);

const planetMat = new THREE.MeshStandardMaterial({
  color: "#5fae5f",
  roughness: 1,
  flatShading: true,
});
const planetGeo = new THREE.IcosahedronGeometry(R, 6);
// pequeñas ondulaciones para aspecto low-poly
const pos = planetGeo.attributes.position;
const tmp = new THREE.Vector3();
for (let i = 0; i < pos.count; i++) {
  tmp.fromBufferAttribute(pos, i);
  const bump = (Math.sin(tmp.x * 1.3) + Math.cos(tmp.z * 1.5) + Math.sin(tmp.y * 1.1)) * 0.18;
  tmp.setLength(R + bump);
  pos.setXYZ(i, tmp.x, tmp.y, tmp.z);
}
planetGeo.computeVertexNormals();
planet.add(new THREE.Mesh(planetGeo, planetMat));

// océano/atmósfera tenue
planet.add(
  new THREE.Mesh(
    new THREE.SphereGeometry(R + 2.4, 32, 32),
    new THREE.MeshBasicMaterial({
      color: "#6fb7ff",
      transparent: true,
      opacity: 0.06,
      side: THREE.BackSide,
    })
  )
);

/* ---------- Utilidades de esfera ---------- */
function latLonToUnit(latDeg, lonDeg) {
  const lat = THREE.MathUtils.degToRad(latDeg);
  const lon = THREE.MathUtils.degToRad(lonDeg);
  return new THREE.Vector3(
    Math.cos(lat) * Math.cos(lon),
    Math.sin(lat),
    Math.cos(lat) * Math.sin(lon)
  ).normalize();
}

// Orienta un objeto para que se apoye en la superficie (su +Y mira al cielo)
function placeOnSurface(obj, unit, radius = R) {
  const up = unit.clone();
  let ref = new THREE.Vector3(0, 1, 0);
  if (Math.abs(up.dot(ref)) > 0.95) ref = new THREE.Vector3(1, 0, 0);
  const z = new THREE.Vector3().crossVectors(ref, up).normalize(); // tangente
  const x = new THREE.Vector3().crossVectors(up, z).normalize();
  const m = new THREE.Matrix4().makeBasis(x, up, z);
  obj.quaternion.setFromRotationMatrix(m);
  obj.position.copy(up.clone().multiplyScalar(radius));
}

/* ---------- Etiquetas flotantes (sprites de texto) ---------- */
function makeLabel(icono, nombre) {
  const c = document.createElement("canvas");
  c.width = 512;
  c.height = 160;
  const ctx = c.getContext("2d");
  ctx.fillStyle = "rgba(10,16,34,0.82)";
  roundRect(ctx, 8, 8, 496, 144, 28);
  ctx.fill();
  ctx.strokeStyle = "rgba(120,150,220,0.6)";
  ctx.lineWidth = 3;
  ctx.stroke();
  ctx.font = "72px serif";
  ctx.textBaseline = "middle";
  ctx.fillText(icono, 34, 84);
  ctx.fillStyle = "#eaf0ff";
  ctx.font = "bold 40px Segoe UI, sans-serif";
  ctx.fillText(nombre, 130, 84);
  const tex = new THREE.CanvasTexture(c);
  tex.anisotropy = 4;
  const spr = new THREE.Sprite(
    new THREE.SpriteMaterial({ map: tex, transparent: true, depthWrite: false })
  );
  spr.scale.set(6.4, 2.0, 1);
  return spr;
}
function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

/* ---------- Constructores de edificios ---------- */
const M = (color, opts = {}) =>
  new THREE.MeshStandardMaterial({ color, roughness: 0.85, flatShading: true, ...opts });
const box = (w, h, d, color, opts) => new THREE.Mesh(new THREE.BoxGeometry(w, h, d), M(color, opts));

function buildHospital() {
  const g = new THREE.Group();
  const b = box(3.2, 3, 2.6, "#eef3f8");
  b.position.y = 1.5;
  g.add(b);
  const roof = box(3.4, 0.4, 2.8, "#cfd9e6");
  roof.position.y = 3.2;
  g.add(roof);
  // cruz roja
  const cv = box(0.4, 1.4, 0.1, "#d33");
  cv.position.set(0, 1.8, 1.32);
  const ch = box(1.4, 0.4, 0.1, "#d33");
  ch.position.set(0, 1.8, 1.32);
  g.add(cv, ch);
  return g;
}
function buildTaller() {
  const g = new THREE.Group();
  const b = box(3.6, 2.4, 3, "#b9c2cc");
  b.position.y = 1.2;
  g.add(b);
  const door = box(2.2, 1.6, 0.1, "#3a4654");
  door.position.set(0, 0.9, 1.51);
  g.add(door);
  // cochecito delante
  const car = box(1.6, 0.6, 0.9, "#d9483b");
  car.position.set(0, 0.4, 2.4);
  const cab = box(0.9, 0.5, 0.8, "#b53a2f");
  cab.position.set(0.1, 0.85, 2.4);
  g.add(car, cab);
  return g;
}
function buildTech() {
  const g = new THREE.Group();
  const b = box(2.8, 3.4, 2.8, "#3b5bdb");
  b.position.y = 1.7;
  g.add(b);
  // ventanas
  for (let i = 0; i < 3; i++) {
    const w = box(2.0, 0.3, 0.05, "#9ec5ff", { emissive: "#3a6", emissiveIntensity: 0 });
    w.position.set(0, 0.9 + i * 0.9, 1.42);
    g.add(w);
  }
  const ant = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.6), M("#dde"));
  ant.position.y = 4.2;
  g.add(ant);
  const ball = new THREE.Mesh(new THREE.SphereGeometry(0.18), M("#ff5252", { emissive: "#ff5252", emissiveIntensity: 0.6 }));
  ball.position.y = 5;
  g.add(ball);
  return g;
}
function buildRestaurante() {
  const g = new THREE.Group();
  const b = box(3.2, 2.6, 2.6, "#f3d2a7");
  b.position.y = 1.3;
  g.add(b);
  // toldo a rayas (simplificado)
  const awn = box(3.4, 0.3, 1.2, "#d9483b");
  awn.position.set(0, 2.5, 1.5);
  awn.rotation.x = -0.3;
  g.add(awn);
  const sign = box(1.4, 0.7, 0.1, "#fff4d6");
  sign.position.set(0, 3.2, 1.0);
  g.add(sign);
  return g;
}
function buildGranja() {
  const g = new THREE.Group();
  const b = box(3.4, 2.2, 2.8, "#c0473b");
  b.position.y = 1.1;
  g.add(b);
  const roof = new THREE.Mesh(new THREE.CylinderGeometry(0.01, 2.2, 1.4, 4), M("#8a342b"));
  roof.position.y = 2.9;
  roof.rotation.y = Math.PI / 4;
  g.add(roof);
  // silo
  const silo = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 3), M("#cdd3da"));
  silo.position.set(2.4, 1.5, 0);
  g.add(silo);
  const cap = new THREE.Mesh(new THREE.ConeGeometry(0.8, 0.8, 12), M("#9aa3ad"));
  cap.position.set(2.4, 3.3, 0);
  g.add(cap);
  return g;
}
function buildElectrica() {
  const g = new THREE.Group();
  const b = box(2.4, 1.8, 2.4, "#d7d2b0");
  b.position.y = 0.9;
  g.add(b);
  // torre/pilón
  const t = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.25, 4, 6), M("#8a8f99"));
  t.position.set(1.6, 2, 0);
  g.add(t);
  const arm = box(2.2, 0.15, 0.15, "#8a8f99");
  arm.position.set(1.6, 3.6, 0);
  g.add(arm);
  // rayo
  const ray = box(0.5, 1.0, 0.08, "#ffd23f", { emissive: "#ffd23f", emissiveIntensity: 0.7 });
  ray.position.set(0, 2.6, 1.3);
  ray.rotation.z = 0.4;
  g.add(ray);
  return g;
}

const BUILDERS = {
  hospital: buildHospital,
  taller: buildTaller,
  tech: buildTech,
  restaurante: buildRestaurante,
  granja: buildGranja,
  electrica: buildElectrica,
};

/* ---------- Colocar edificios en el planeta ---------- */
const spots = [
  [18, 0],
  [-12, 60],
  [25, 130],
  [-30, 200],
  [10, 250],
  [-5, 310],
];
const buildings = []; // { data, unit, worldPos }
FP_BUILDINGS.forEach((data, i) => {
  const [lat, lon] = spots[i % spots.length];
  const unit = latLonToUnit(lat, lon);
  const g = BUILDERS[data.type]();
  placeOnSurface(g, unit);
  planet.add(g);

  const label = makeLabel(data.icono, data.nombre.split(" · ")[0]);
  label.position.copy(unit.clone().multiplyScalar(R + 7.5));
  planet.add(label);

  buildings.push({ data, unit, worldPos: unit.clone().multiplyScalar(R + 2) });
});

/* ---------- Árboles de decoración ---------- */
(function scatterTrees() {
  for (let i = 0; i < 60; i++) {
    const unit = new THREE.Vector3().randomDirection();
    // evitar superponer con edificios
    if (buildings.some((b) => unit.angleTo(b.unit) < 0.18)) continue;
    const t = new THREE.Group();
    const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.16, 0.7), M("#6b4a2b"));
    trunk.position.y = 0.35;
    const leaf = new THREE.Mesh(new THREE.ConeGeometry(0.6, 1.2, 7), M("#2f8f4e"));
    leaf.position.y = 1.1;
    t.add(trunk, leaf);
    t.scale.setScalar(0.7 + Math.random() * 0.8);
    placeOnSurface(t, unit);
    planet.add(t);
  }
})();

/* ---------- Personaje / mensajero ---------- */
const player = new THREE.Group();
scene.add(player);
(function buildPlayer() {
  const body = new THREE.Mesh(new THREE.CapsuleGeometry(0.4, 0.7, 4, 8), M("#3a6ff7"));
  body.position.y = 0.85;
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.34, 16, 16), M("#ffd9b0"));
  head.position.y = 1.6;
  const cap = new THREE.Mesh(new THREE.SphereGeometry(0.36, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2), M("#c8102e"));
  cap.position.y = 1.7;
  // mochila de mensajero
  const bag = box(0.5, 0.5, 0.25, "#e0a040");
  bag.position.set(0, 0.95, -0.45);
  player.add(body, head, cap, bag);
})();

/* ---------- Brújula 3D que persigue al jugador ---------- */
const compass = new THREE.Group();
scene.add(compass);
const compassRing = new THREE.Mesh(
  new THREE.TorusGeometry(0.85, 0.12, 12, 28),
  M("#e8c14a", { metalness: 0.4, roughness: 0.4 })
);
const compassFace = new THREE.Mesh(
  new THREE.CircleGeometry(0.78, 28),
  new THREE.MeshStandardMaterial({ color: "#10203f", roughness: 0.5 })
);
compass.add(compassRing, compassFace);

// aguja: Object3D.lookAt orienta el +Z hacia el objetivo, así que la punta mira a +Z
const needle = new THREE.Group();
const tip = new THREE.Mesh(new THREE.ConeGeometry(0.18, 0.7, 12), M("#ff4d4d", { emissive: "#ff4d4d", emissiveIntensity: 0.3 }));
tip.rotation.x = Math.PI / 2; // cono +Y -> +Z (hacia el edificio)
tip.position.z = 0.35;
const tail = new THREE.Mesh(new THREE.ConeGeometry(0.18, 0.6, 12), M("#dfe6ff"));
tail.rotation.x = -Math.PI / 2; // -> -Z
tail.position.z = -0.3;
needle.add(tip, tail);
const hub = new THREE.Mesh(new THREE.SphereGeometry(0.14), M("#fff"));
needle.add(hub);
compass.add(needle);
compass.position.set(0, R + 12, 0);

/* ---------- Estado del jugador en la esfera ---------- */
const playerUp = new THREE.Vector3(0, 1, 0);
const playerFwd = new THREE.Vector3(0, 0, 1);
const MOVE = 0.9; // rad/s
const TURN = 2.0; // rad/s

const keys = {};
const setKey = (k, v) => (keys[k] = v);
window.addEventListener("keydown", (e) => mapKey(e.code, true));
window.addEventListener("keyup", (e) => mapKey(e.code, false));
function mapKey(code, v) {
  if (["ArrowUp", "KeyW"].includes(code)) setKey("forward", v);
  if (["ArrowDown", "KeyS"].includes(code)) setKey("back", v);
  if (["ArrowLeft", "KeyA"].includes(code)) setKey("left", v);
  if (["ArrowRight", "KeyD"].includes(code)) setKey("right", v);
}
// botones táctiles
document.querySelectorAll(".btn").forEach((b) => {
  const k = b.dataset.key;
  const on = (e) => { e.preventDefault(); setKey(k, true); };
  const off = (e) => { e.preventDefault(); setKey(k, false); };
  b.addEventListener("pointerdown", on);
  b.addEventListener("pointerup", off);
  b.addEventListener("pointerleave", off);
  b.addEventListener("pointercancel", off);
});

/* ---------- Panel de información ---------- */
const panel = document.getElementById("panel");
const objetivo = document.getElementById("objetivo");
let currentNearId = null;
let walkPhase = 0;

document.getElementById("panel-close").addEventListener("click", () => {
  panel.classList.add("hidden");
  // marcar para no reabrir hasta alejarse
  currentNearId = "__closed__";
});

function showPanel(d) {
  document.getElementById("panel-icono").textContent = d.icono;
  document.getElementById("panel-nombre").textContent = d.nombre.split(" · ")[1] || d.nombre;
  document.getElementById("panel-familia").textContent = d.familia;
  document.getElementById("panel-descripcion").textContent = d.descripcion;
  document.getElementById("panel-duracion").textContent = d.duracion;
  document.getElementById("panel-salidas").textContent = d.salidas;
  const niv = document.getElementById("panel-niveles");
  niv.innerHTML = "";
  d.niveles.forEach((n) => {
    const s = document.createElement("span");
    s.className = "nivel-chip";
    s.textContent = n;
    niv.appendChild(s);
  });
  const ul = document.getElementById("panel-ciclos");
  ul.innerHTML = "";
  d.ciclos.forEach((c) => {
    const li = document.createElement("li");
    li.textContent = c;
    ul.appendChild(li);
  });
  panel.classList.remove("hidden");
}

/* ---------- Bucle ---------- */
const clock = new THREE.Clock();
let started = false;

function tick() {
  const dt = Math.min(clock.getDelta(), 0.05);

  // --- movimiento sobre la esfera ---
  let moving = false;
  if (started) {
    const xAxis = new THREE.Vector3().crossVectors(playerUp, playerFwd).normalize();
    if (keys.forward || keys.back) {
      const d = (keys.forward ? 1 : -1) * MOVE * dt;
      const q = new THREE.Quaternion().setFromAxisAngle(xAxis, d);
      playerUp.applyQuaternion(q).normalize();
      playerFwd.applyQuaternion(q).normalize();
      moving = true;
    }
    if (keys.left || keys.right) {
      const t = (keys.left ? 1 : -1) * TURN * dt;
      const q = new THREE.Quaternion().setFromAxisAngle(playerUp, t);
      playerFwd.applyQuaternion(q).normalize();
    }
    // reortonormalizar
    playerFwd.addScaledVector(playerUp, -playerFwd.dot(playerUp)).normalize();
  }

  // colocar personaje
  const xA = new THREE.Vector3().crossVectors(playerUp, playerFwd).normalize();
  const basis = new THREE.Matrix4().makeBasis(xA, playerUp, playerFwd);
  player.quaternion.setFromRotationMatrix(basis);
  const surface = playerUp.clone().multiplyScalar(R + 0.1);
  player.position.copy(surface);
  // bobbing al caminar
  walkPhase += moving ? dt * 10 : 0;
  player.position.addScaledVector(playerUp, moving ? Math.abs(Math.sin(walkPhase)) * 0.15 : 0);

  // --- cámara siguiendo por detrás ---
  const camTarget = surface
    .clone()
    .addScaledVector(playerUp, 7)
    .addScaledVector(playerFwd, -11);
  camera.position.lerp(camTarget, started ? 0.08 : 0.02);
  camera.up.copy(playerUp);
  camera.lookAt(surface.clone().addScaledVector(playerUp, 1.5));

  // --- edificio más cercano ---
  let nearest = null;
  let nearestAng = Infinity;
  for (const b of buildings) {
    const ang = playerUp.angleTo(b.unit);
    if (ang < nearestAng) {
      nearestAng = ang;
      nearest = b;
    }
  }

  // --- brújula que persigue al jugador ---
  const chase = surface
    .clone()
    .addScaledVector(playerUp, 3.2)
    .addScaledVector(xA, 2.0)
    .addScaledVector(playerUp, Math.sin(performance.now() * 0.002) * 0.3);
  compass.position.lerp(chase, 0.06);
  compassRing.lookAt(camera.position);
  compassFace.lookAt(camera.position);
  if (nearest) needle.lookAt(nearest.worldPos);

  // --- proximidad / panel ---
  const NEAR = 0.16; // umbral angular
  if (nearest && nearestAng < NEAR) {
    if (currentNearId !== nearest.data.id && currentNearId !== "__closed__") {
      currentNearId = nearest.data.id;
      showPanel(nearest.data);
    }
    objetivo.textContent = `Estás en: ${nearest.data.nombre.split(" · ")[0]}`;
  } else {
    if (currentNearId) {
      currentNearId = null;
      panel.classList.add("hidden");
    }
    if (nearest) {
      const km = (nearestAng * R).toFixed(0);
      objetivo.textContent = `🧭 Edificio más cercano: ${nearest.data.nombre.split(" · ")[0]} (${km} u.)`;
    }
  }

  // rotación suave del planeta cuando aún no se ha empezado (preview)
  if (!started) planet.rotation.y += dt * 0.1;

  renderer.render(scene, camera);
  requestAnimationFrame(tick);
}
tick();

/* ---------- Inicio ---------- */
document.getElementById("start").addEventListener("click", () => {
  document.getElementById("intro").classList.add("hidden");
  planet.rotation.set(0, 0, 0);
  started = true;
});

/* ---------- Resize ---------- */
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
