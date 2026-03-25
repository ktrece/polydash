import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove global style block for mobile overrides completely
c = re.sub(r'<style>\s*\.custom-scrollbar.*?</style>', '<style>\n        .custom-scrollbar::-webkit-scrollbar { width: 4px; }\n        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }\n        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.8); border-radius: 4px; }\n        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(71, 85, 105, 1); }\n    </style>', c, flags=re.DOTALL)
c = re.sub(r'@media\s*\(max-width:\s*768px\).*?}\s*}', '', c, flags=re.DOTALL)

# 2. Replace Header
header_match = re.search(r'<header.*?</header>', c, re.DOTALL)
if header_match:
    old_h = header_match.group(0)
    new_h = """    <header class="bg-[#1e293b] border-b border-slate-700 flex flex-col md:flex-row items-center justify-between px-4 py-2 md:py-0 shrink-0 shadow-md z-30 relative md:h-14">
        <div class="flex items-center justify-between w-full md:w-auto gap-3">
            <div class="flex items-center gap-3">
                <div class="cursor-pointer hover:opacity-80 transition-opacity flex items-center justify-center min-w-[44px] min-h-[44px]" onclick="resetBalanceCalibration()" title="Click para Recalibrar Saldos">
                    <img src="profile-image-5936167-467b5244-f7ba-4793-b3ab-9da426f18e60.webp" alt="Bot Logo" class="w-11 h-11 md:w-11 md:h-11 rounded-full border border-indigo-500/50 shadow-sm object-cover">
                </div>
                <div class="flex flex-col border-r border-slate-600 pr-3 pl-2 justify-center min-h-[44px]">
                    <span class="text-[11px] md:text-[8px] text-slate-400 font-bold uppercase tracking-wider leading-tight" title="Dinero Total">Portfolio</span>
                    <span class="text-[16px] md:text-[12px] font-black text-indigo-400 tracking-wide leading-tight" id="portfolio-balance">--</span>
                </div>
                <div class="flex flex-col md:border-r border-slate-600 pr-3 cursor-pointer hover:opacity-80 transition-opacity justify-center min-h-[44px]" onclick="window.open('liquidez-historial.html', '_blank')" title="Ver Historial de Liquidez">
                    <span class="text-[11px] md:text-[8px] text-slate-400 font-bold uppercase tracking-wider flex items-center gap-1 leading-tight">Available <span class="text-[14px] md:text-[10px] leading-none text-emerald-400/70">↗</span></span>
                    <span class="text-[16px] md:text-[12px] font-black text-emerald-400 tracking-wide leading-tight" id="available-balance">--</span>
                </div>
            </div>
            
            <button id="hamburger-btn" class="md:hidden flex flex-col justify-center items-center w-11 h-11 bg-slate-700/50 rounded border border-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                <span class="w-6 h-0.5 bg-slate-200 mb-1.5 transition-transform duration-300 origin-center" id="bar1"></span>
                <span class="w-6 h-0.5 bg-slate-200 mb-1.5 transition-opacity duration-300" id="bar2"></span>
                <span class="w-6 h-0.5 bg-slate-200 transition-transform duration-300 origin-center" id="bar3"></span>
            </button>
        </div>

        <div id="nav-menu" class="hidden md:flex flex-col md:flex-row items-stretch md:items-center gap-0 md:gap-4 w-full md:w-auto bg-[#1e293b] md:bg-transparent absolute md:static top-full left-0 border-b border-slate-700 md:border-none shadow-xl md:shadow-none z-20">
            <div class="flex flex-wrap md:flex-nowrap items-center justify-between md:justify-start gap-4 md:gap-3 border-b md:border-b-0 md:border-r border-slate-700 md:border-slate-600 px-4 py-4 md:px-0 md:py-0 md:pr-4">
                <div class="flex flex-col items-center">
                    <span class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">Apuesta</span>
                    <span class="text-[14px] md:text-[10px] font-bold text-teal-400 leading-tight" id="cfg-normal">--</span>
                </div>
                <div class="flex flex-col items-center">
                    <span class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">Tras Perd.</span>
                    <span class="text-[14px] md:text-[10px] font-bold text-teal-400 leading-tight" id="cfg-tras-perdida">--</span>
                </div>
                <div class="flex flex-col items-center">
                    <span class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold"># Apuestas</span>
                    <span class="text-[14px] md:text-[10px] font-bold text-teal-400 leading-tight" id="cfg-num-perdida">--</span>
                </div>
                <div class="flex flex-col items-center">
                    <span class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">% Salida</span>
                    <span class="text-[14px] md:text-[10px] font-bold text-teal-400 leading-tight" id="cfg-salida">--</span>
                </div>
                <div class="flex flex-col items-center">
                    <span class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">Desde</span>
                    <div class="flex flex-col items-center leading-none">
                        <span class="text-[14px] md:text-[10px] font-mono font-bold text-slate-300" id="cfg-desde">--</span>
                        <span class="text-[11px] md:text-[7px] text-slate-500 font-medium tracking-wide mt-0.5" id="cfg-desde-fecha">--</span>
                    </div>
                </div>
                <a href="configuraciones.html" target="_blank" class="flex items-center justify-center w-11 h-11 md:w-auto md:h-auto md:ml-1 text-[16px] md:text-[8px] bg-teal-500/10 text-teal-400 hover:bg-teal-500/20 md:px-2 md:py-1 rounded border border-teal-500/30 transition-colors font-bold uppercase" title="Ajustes de Configuración">⚙️</a>
            </div>

            <div id="ping-indicator" class="flex items-center justify-between md:justify-center gap-2 border-b md:border-b-0 md:border-r border-slate-700 md:border-slate-600 px-4 py-3 md:px-0 md:py-0 md:pr-4 h-auto md:h-8" title="Latencia de conexión">
                <span class="text-[13px] md:hidden text-slate-400 font-bold uppercase tracking-wider">Latencia</span>
                <div class="flex items-center gap-1.5">
                    <span class="w-2 h-2 md:w-1.5 md:h-1.5 rounded-full bg-slate-500 animate-pulse"></span>
                    <span class="text-[13px] md:text-[10px] font-bold text-slate-400 font-mono">-- ms</span>
                </div>
            </div>

            <div id="last-update" class="hidden flex items-center justify-between md:flex-col md:items-end md:justify-center border-b md:border-b-0 md:border-r border-slate-700 md:border-slate-600 px-4 py-3 md:px-0 md:py-0 md:pr-4 h-auto md:h-8">
                <span class="text-[13px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">Última Operación</span>
                <span id="last-update-time" class="text-[14px] md:text-[10px] font-bold text-blue-300 leading-tight">--</span>
            </div>
            
            <div id="data-counter" class="hidden flex items-center justify-between md:justify-start gap-3 border-b md:border-b-0 md:border-r border-slate-700 md:border-slate-600 px-4 py-3 md:px-0 md:py-0 md:pr-4 h-auto md:h-8">
                <div class="flex flex-col md:items-end justify-center">
                    <span class="text-[13px] md:text-[8px] text-slate-400 uppercase tracking-wider font-bold">Base de Datos</span>
                    <span class="text-[14px] md:text-[10px] font-bold text-slate-200 leading-tight"><span id="total-rows">0</span> registros</span>
                </div>
                <button id="clear-data-btn" onclick="handleClearData()" class="flex items-center justify-center w-11 h-11 md:w-auto md:h-auto bg-red-500/10 hover:bg-red-500/20 border border-red-500/30 text-red-400 md:p-1 rounded transition-colors" title="Purgar Base de Datos">
                    <span class="text-xl md:text-xs leading-none">🗑️</span>
                </button>
            </div>

            <div class="flex flex-col md:flex-row items-stretch md:items-center justify-around md:justify-start gap-3 px-4 py-4 md:px-0 md:py-0">
                <input type="file" id="fileInput" accept=".csv" class="hidden" multiple />
                <button onclick="document.getElementById('fileInput').click()" class="flex flex-1 md:flex-none items-center justify-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white min-h-[44px] md:min-h-0 md:px-2 md:py-1.5 rounded-md text-[13px] md:text-[10px] font-bold uppercase tracking-wider transition-colors border border-indigo-500 shadow-lg shadow-indigo-900/20" title="Cargar CSV">
                    <span class="text-xl md:text-sm leading-none">📁</span>
                    <span class="md:hidden">Cargar CSV</span>
                </button>
                <button onclick="downloadDashboard()" class="flex flex-1 md:flex-none items-center justify-center gap-2 bg-slate-700 hover:bg-slate-600 text-slate-200 min-h-[44px] md:min-h-0 md:px-2 md:py-1.5 rounded-md text-[13px] md:text-[10px] font-bold uppercase tracking-wider transition-colors border border-slate-600 shadow-lg" title="Exportar Dashboard">
                    <span class="text-xl md:text-sm leading-none">📸</span>
                    <span class="md:hidden">Exportar</span>
                </button>
                <button onclick="window.open('historial-operaciones.html','_blank')" class="flex flex-1 md:flex-none items-center justify-center gap-2 bg-slate-700 hover:bg-slate-600 text-slate-200 min-h-[44px] md:min-h-0 md:px-2 md:py-1.5 rounded-md text-[13px] md:text-[10px] font-bold uppercase tracking-wider transition-colors border border-slate-600 shadow-lg" title="Historial de Operaciones">
                    <span class="text-xl md:text-sm leading-none">⏱️</span>
                    <span class="md:hidden">Historial</span>
                </button>
            </div>
        </div>
    </header>"""
    c = c.replace(old_h, new_h)

# 3. Remove old mobile action bar if exists
c = re.sub(r'<!-- MOBILE ACTION BAR.*?</div>', '', c, flags=re.DOTALL)

# 4. Update Main tags & Sections
main_match = re.search(r'<main.*?</main>', c, flags=re.DOTALL)
if main_match:
    main_content = main_match.group(0)
    
    # Update main container
    main_content = re.sub(r'<main class="[^"]*"', '<main class="flex-1 flex flex-col md:grid md:grid-cols-12 gap-6 md:gap-3 p-4 md:p-3 bg-[#0f172a] overflow-y-auto md:overflow-hidden min-h-0 pb-28 md:pb-3 w-full"', main_content)
    
    # Core bot
    main_content = re.sub(r'<section id="core-bot" class="[^"]*"', '<section id="core-bot" class="w-full md:col-span-3 flex flex-col gap-4 md:gap-3 min-h-0 shrink-0 md:shrink"', main_content)
    main_content = re.sub(r'<div class="px-3 py-2 border-b border-slate-700 flex justify-between items-center bg-slate-800/50 rounded-t-xl">', '<div class="px-4 py-3 md:px-3 md:py-2 border-b border-slate-700 flex justify-between items-center bg-slate-800/50 rounded-t-xl">', main_content)
    main_content = re.sub(r'<h2 class="text-\[10px\] font-bold text-indigo-400', '<h2 class="text-[14px] md:text-[10px] font-bold text-indigo-400', main_content)
    main_content = re.sub(r'<span class="leading-none">⚡</span>', '<span class="leading-none text-lg md:text-base">⚡</span>', main_content)
    main_content = re.sub(r'<span class="text-\[8px\] bg-indigo-500/10', '<span class="text-[12px] md:text-[8px] bg-indigo-500/10 px-2 py-1 md:px-1.5 md:py-0.5', main_content)
    main_content = re.sub(r'<span class="text-\[7px\] text-slate-500', '<span class="text-[10px] md:text-[7px] mt-1 md:mt-0.5 text-slate-500', main_content)
    main_content = re.sub(r'<div id="bot-metrics" class="p-3 grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-2">', '<div id="bot-metrics" class="p-4 md:p-2.5 grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-2">', main_content)
    
    # Proyecciones
    main_content = re.sub(r'<div class="bg-\[#1e293b\] rounded-xl border border-slate-700 flex flex-col md:flex-1 shrink-0 md:shrink min-h-0 shadow-lg">', '<div class="bg-[#1e293b] rounded-xl border border-slate-700 flex flex-col md:flex-1 shrink-0 md:shrink min-h-0 shadow-lg">', main_content)
    main_content = re.sub(r'<div class="px-3 py-2 border-b border-slate-700 bg-slate-800/50 rounded-t-xl shrink-0">', '<div class="px-4 py-3 md:px-3 md:py-2 border-b border-slate-700 bg-slate-800/50 rounded-t-xl shrink-0">', main_content)
    main_content = re.sub(r'<h2 class="text-\[10px\] font-bold text-emerald-400', '<h2 class="text-[14px] md:text-[10px] font-bold text-emerald-400', main_content)
    main_content = re.sub(r'<span class="leading-none">🚀</span>', '<span class="leading-none text-lg md:text-base">🚀</span>', main_content)
    main_content = re.sub(r'<div id="projections-content" class="p-3 flex-1 flex flex-col min-h-\[200px\] md:min-h-0 overflow-y-visible md:overflow-y-auto custom-scrollbar">', '<div id="projections-content" class="p-4 md:p-2.5 flex-1 flex flex-col min-h-[150px] md:min-h-0 overflow-y-visible md:overflow-y-auto custom-scrollbar">', main_content)
    
    # Auditoria
    main_content = re.sub(r'<section id="auditoria" class="[^"]*"', '<section id="auditoria" class="w-full md:col-span-4 flex flex-col gap-4 md:gap-3 min-h-0 shrink-0 md:shrink"', main_content)
    main_content = re.sub(r'<div class="px-3 py-2 border-b border-slate-700 bg-slate-800/50 rounded-t-xl shrink-0 flex justify-between items-center">', '<div class="px-4 py-3 md:px-3 md:py-2 border-b border-slate-700 bg-slate-800/50 rounded-t-xl shrink-0 flex justify-between items-center">', main_content)
    main_content = re.sub(r'<h2 class="text-\[10px\] font-bold text-orange-400', '<h2 class="text-[14px] md:text-[10px] font-bold text-orange-400', main_content)
    main_content = re.sub(r'<span class="leading-none">🕵️</span>', '<span class="leading-none text-lg md:text-base">🕵️</span>', main_content)
    main_content = re.sub(r'<span id="loss-free-counter" class="text-\[8px\]', '<span id="loss-free-counter" class="text-[12px] md:text-[8px]', main_content)
    main_content = re.sub(r'<div id="expert-analysis" class="p-3 flex flex-col overflow-visible md:overflow-hidden">', '<div id="expert-analysis" class="p-4 md:p-3 flex flex-col overflow-visible md:overflow-hidden">', main_content)
    
    # Chart
    main_content = re.sub(r'<h2 id="chartTitle" onclick="openDetailedChart\(\)" class="text-\[10px\]', '<h2 id="chartTitle" onclick="openDetailedChart()" class="text-[14px] md:text-[10px] min-h-[44px] md:min-h-0 text-center flex-1 justify-center', main_content)
    main_content = re.sub(r'<span class="leading-none" id="chartIcon">📊</span>', '<span class="leading-none text-lg md:text-base" id="chartIcon">📊</span>', main_content)
    main_content = re.sub(r'<button onclick="toggleChart\(\)" class="text-slate-400 hover:text-white px-2 py-0.5', '<button onclick="toggleChart()" class="text-slate-400 hover:text-white flex items-center justify-center min-w-[44px] min-h-[44px] md:min-w-0 md:min-h-0 md:px-2 md:py-0.5 text-lg md:text-xs', main_content)
    main_content = re.sub(r'<div id="chartLegend" class="px-3 py-1.5', '<div id="chartLegend" class="px-4 py-3 md:px-3 md:py-1.5 text-[12px] md:text-[9px]', main_content)
    main_content = re.sub(r'<div id="dailyChartContainer" class="p-3 flex-1 flex flex-col min-h-\[250px\] md:min-h-0 relative pt-8">', '<div id="dailyChartContainer" class="p-4 md:p-3 flex-1 flex flex-col min-h-[250px] md:min-h-0 relative pt-10 md:pt-8">', main_content)
    main_content = re.sub(r'<div id="dailyChartDate" class="absolute top-2 left-0 right-0 text-center text-\[10px\]', '<div id="dailyChartDate" class="absolute top-2 left-0 right-0 text-center text-[12px] md:text-[10px]', main_content)
    
    # Historial
    main_content = re.sub(r'<section id="historial-global" class="[^"]*"', '<section id="historial-global" class="w-full md:col-span-5 flex flex-col min-h-0 shrink-0 md:shrink"', main_content)
    main_content = re.sub(r'<h2 class="text-\[10px\] font-bold text-blue-400', '<h2 class="text-[14px] md:text-[10px] font-bold text-blue-400', main_content)
    main_content = re.sub(r'<span class="leading-none">🌍</span>', '<span class="leading-none text-lg md:text-base">🌍</span>', main_content)
    main_content = re.sub(r'<span class="text-\[8px\] text-slate-400', '<span class="text-[12px] md:text-[8px] text-slate-400', main_content)
    main_content = re.sub(r'<div id="results" class="p-3 grid grid-cols-1 md:grid-cols-2', '<div id="results" class="p-4 md:p-3 grid grid-cols-1 md:grid-cols-2', main_content)
    
    c = c.replace(main_match.group(0), main_content)

# 5. Bottom Navbar sizes
nav_match = re.search(r'<div class="md:hidden fixed bottom-0 w-full.*?>.*?</div>', c, flags=re.DOTALL)
if nav_match:
    old_nav = nav_match.group(0)
    new_nav = '''<div class="md:hidden fixed bottom-0 w-full bg-[#1e293b] border-t border-slate-700 flex justify-around items-center p-2 pb-6 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.3)] z-50">
        <button onclick="document.getElementById('core-bot').scrollIntoView({behavior:'smooth'})" class="text-slate-200 flex flex-col items-center justify-center text-[12px] min-w-[60px] min-h-[44px]">
            <span class="text-2xl mb-1">⚡</span>
            <span class="font-bold">Bot</span>
        </button>
        <button onclick="document.getElementById('auditoria').scrollIntoView({behavior:'smooth'})" class="text-slate-200 flex flex-col items-center justify-center text-[12px] min-w-[60px] min-h-[44px]">
            <span class="text-2xl mb-1">🕵️</span>
            <span class="font-bold">Riesgo</span>
        </button>
        <button onclick="document.getElementById('historial-global').scrollIntoView({behavior:'smooth'})" class="text-slate-200 flex flex-col items-center justify-center text-[12px] min-w-[60px] min-h-[44px]">
            <span class="text-2xl mb-1">🌍</span>
            <span class="font-bold">Historial</span>
        </button>
        <a href="perdidas.html" target="_blank" class="text-slate-200 flex flex-col items-center justify-center text-[12px] min-w-[60px] min-h-[44px]">
            <span class="text-2xl mb-1">💥</span>
            <span class="font-bold">Pérdidas</span>
        </a>
    </div>'''
    c = c.replace(old_nav, new_nav)

# 6. Replace JS HTML strings for formatting and responsiveness
c = c.replace('class="text-[10px] opacity-70 font-normal', 'class="text-[12px] md:text-[8px] opacity-70 font-normal')

c = c.replace('class="bg-[#0f172a] p-1.5 rounded border border-slate-700 flex flex-col justify-center items-center text-center"', 'class="bg-[#0f172a] p-3 md:p-1.5 rounded-xl md:rounded border border-slate-700 flex flex-col justify-center items-center text-center"')
c = c.replace('class="text-[8px] text-slate-400 uppercase tracking-wider mb-0.5"', 'class="text-[11px] md:text-[8px] text-slate-400 uppercase tracking-wider mb-1 md:mb-0.5"')
c = c.replace('class="text-[10px] font-black text-slate-200"', 'class="text-[14px] md:text-[10px] font-black text-slate-200"')
c = c.replace('class="text-[10px] font-bold text-slate-200"', 'class="text-[14px] md:text-[10px] font-bold text-slate-200"')
c = c.replace('class="text-[10px] font-bold text-red-400"', 'class="text-[14px] md:text-[10px] font-bold text-red-400"')
c = c.replace('class="text-[10px] font-bold text-emerald-400"', 'class="text-[14px] md:text-[10px] font-bold text-emerald-400"')

# Beneficio Neto
c = c.replace('class="col-span-2 bg-indigo-500/10 p-2 rounded-lg border border-indigo-500/30 flex justify-between items-center mt-0.5"', 'class="col-span-1 md:col-span-2 bg-indigo-500/10 p-4 md:p-2 rounded-xl md:rounded-lg border border-indigo-500/30 flex justify-between items-center mt-2 md:mt-0.5 min-h-[44px]"')
c = c.replace('class="text-[8px] font-bold text-indigo-300', 'class="text-[12px] md:text-[8px] font-bold text-indigo-300')
c = c.replace('class="text-[7px] text-indigo-200', 'class="text-[11px] md:text-[7px] text-indigo-200')

# Proyecciones HTML strings in JS
c = c.replace('class="bg-indigo-500/10 p-2 rounded border border-indigo-500/20 mb-2', 'class="bg-indigo-500/10 p-4 md:p-2 rounded-xl md:rounded border border-indigo-500/20 mb-4 md:mb-2')
c = c.replace('class="grid grid-cols-3 gap-2 flex-1"', 'class="grid grid-cols-1 md:grid-cols-3 gap-3 md:gap-2 flex-1"')
c = c.replace('class="bg-[#0f172a] p-2 rounded border border-slate-700 flex flex-col items-center justify-center gap-1"', 'class="bg-[#0f172a] p-4 md:p-2 rounded-xl md:rounded border border-slate-700 flex flex-col items-center justify-center gap-1.5 md:gap-1"')

# Top Losers HTML strings in JS
c = c.replace('class="block bg-[#0f172a] p-1.5 rounded border border-slate-700', 'class="block bg-[#0f172a] p-3 md:p-1.5 rounded-xl md:rounded border border-slate-700 min-h-[44px]')
c = c.replace('class="flex justify-between items-center gap-2"', 'class="flex flex-col md:flex-row md:justify-between md:items-center gap-2"')
c = c.replace('class="text-[9px] text-slate-300 truncate pr-2', 'class="text-[14px] md:text-[9px] text-slate-300 truncate pr-2 leading-tight')
c = c.replace('class="flex items-center gap-2 shrink-0"', 'class="flex items-center justify-between md:justify-end gap-3 md:gap-2 shrink-0"')
c = c.replace('class="text-[9px] bg-blue-900/30 text-blue-300 hover:bg-blue-900/50 hover:text-blue-200 px-1.5 py-0.5 rounded border border-blue-700/50"', 'class="text-[12px] md:text-[9px] bg-blue-900/30 text-blue-300 hover:bg-blue-900/50 hover:text-blue-200 px-3 py-2 md:px-1.5 md:py-0.5 rounded border border-blue-700/50 flex items-center justify-center min-h-[44px] md:min-h-0"')

# Analysis HTML
c = c.replace('class="grid grid-cols-2 gap-2 shrink-0"', 'class="grid grid-cols-1 md:grid-cols-2 gap-3 md:gap-2 shrink-0"')
c = c.replace('class="bg-[#0f172a] p-2 rounded-lg border border-slate-700', 'class="bg-[#0f172a] p-4 md:p-2 rounded-xl md:rounded-lg border border-slate-700 min-h-[44px]')
c = c.replace('class="text-[8px] text-slate-400 uppercase tracking-wider group-hover:text-red-300', 'class="text-[12px] md:text-[8px] text-slate-400 uppercase tracking-wider group-hover:text-red-300')
c = c.replace('<span class="text-[10px] leading-none opacity-0 group-hover:opacity-100', '<span class="text-[14px] md:text-[10px] leading-none md:opacity-0 group-hover:opacity-100')
c = c.replace('class="text-[10px] font-bold text-red-400"', 'class="text-[16px] md:text-[10px] font-bold text-red-400"')
c = c.replace('class="text-[8px] text-slate-600"', 'class="text-[12px] md:text-[8px] text-slate-600"')
c = c.replace('class="text-[10px] font-bold text-slate-200"', 'class="text-[16px] md:text-[10px] font-bold text-slate-200"')
c = c.replace('class="text-[10px] font-bold text-orange-400"', 'class="text-[16px] md:text-[10px] font-bold text-orange-400"')

# Results Cards
c = c.replace('class="flex justify-between items-center w-full bg-[#0f172a] rounded p-1 border border-slate-700/50"', 'class="flex justify-between items-center w-full bg-[#0f172a] rounded-lg md:rounded p-1 border border-slate-700/50 min-h-[44px] md:min-h-0"')
c = c.replace('class="px-2 py-0.5 text-slate-400 hover:text-white transition-colors bg-slate-800 rounded-sm"', 'class="px-4 py-2 md:px-2 md:py-0.5 text-slate-400 hover:text-white transition-colors bg-slate-800 rounded md:rounded-sm flex items-center justify-center min-w-[44px] min-h-[44px] md:min-w-0 md:min-h-0"')
c = c.replace('class="bg-transparent text-slate-300 text-[9px] font-mono text-center outline-none cursor-pointer flex-1 mx-2"', 'class="bg-transparent text-slate-300 text-[14px] md:text-[9px] font-mono text-center outline-none cursor-pointer flex-1 mx-2 min-h-[44px] md:min-h-0"')

c = c.replace('class="flex justify-between items-start mb-2 relative z-10 gap-2"', 'class="flex justify-between items-start mb-4 md:mb-2 relative z-10 gap-2"')
c = c.replace('class="text-[10px] font-bold text-slate-200 flex items-center gap-1.5 uppercase tracking-wider drop-shadow-md w-full"', 'class="text-[14px] md:text-[10px] font-bold text-slate-200 flex flex-col md:flex-row md:items-center gap-2 md:gap-1.5 uppercase tracking-wider drop-shadow-md w-full"')

c = c.replace('class="grid grid-cols-2 gap-2 mb-2 relative z-10 flex-1"', 'class="grid grid-cols-2 gap-3 md:gap-2 mb-4 md:mb-2 relative z-10 flex-1"')
c = c.replace('class="bg-[#0f172a]/80 p-1.5 rounded border border-slate-700/50 flex flex-col justify-center"', 'class="bg-[#0f172a]/80 p-3 md:p-1.5 rounded-lg md:rounded border border-slate-700/50 flex flex-col justify-center"')

c = c.replace('class="bg-slate-800/80 p-2 rounded border border-slate-600 flex justify-between items-center relative z-10 mt-auto"', 'class="bg-slate-800/80 p-4 md:p-2 rounded-xl md:rounded border border-slate-600 flex justify-between items-center relative z-10 mt-auto min-h-[44px] md:min-h-0"')

c = c.replace('class="bg-[#0f172a]/50 rounded-lg border ${p.color} flex flex-col p-2.5 h-full relative overflow-hidden shadow-sm"', 'class="bg-[#0f172a]/50 rounded-2xl md:rounded-lg border ${p.color} flex flex-col p-4 md:p-2.5 h-full relative overflow-hidden shadow-sm"')

c = c.replace('class="mt-2 grid grid-cols-2 gap-2"', 'class="mt-3 md:mt-2 grid grid-cols-1 md:grid-cols-2 gap-3 md:gap-2"')
c = c.replace('class="bg-[#1e293b] p-1.5 rounded border border-slate-700 flex justify-between items-center"', 'class="bg-[#1e293b] p-3 md:p-1.5 rounded-xl md:rounded border border-slate-700 flex justify-between items-center min-h-[44px] md:min-h-0"')

# Add hamburger toggle script to DOMContentLoaded
script_injection = """
        // Hamburger menu toggle
        document.addEventListener('DOMContentLoaded', () => {
            const btn = document.getElementById('hamburger-btn');
            const menu = document.getElementById('nav-menu');
            const bar1 = document.getElementById('bar1');
            const bar2 = document.getElementById('bar2');
            const bar3 = document.getElementById('bar3');

            if(btn && menu) {
                btn.addEventListener('click', () => {
                    menu.classList.toggle('hidden');
                    menu.classList.toggle('flex');
                    bar1.classList.toggle('translate-y-2');
                    bar1.classList.toggle('rotate-45');
                    bar2.classList.toggle('opacity-0');
                    bar3.classList.toggle('-translate-y-2');
                    bar3.classList.toggle('-rotate-45');
                });
            }
        });
"""
if 'const EUR_RATE = 0.92;' in c:
    c = c.replace('const EUR_RATE = 0.92;', script_injection + '\n        const EUR_RATE = 0.92;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
