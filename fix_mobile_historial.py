import re

with open('historial-operaciones.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Make inputs and selects min-h-[44px] on mobile
c = c.replace('class="bg-slate-800 text-slate-200 text-[12px] px-2 py-1 rounded border border-slate-700"', 'class="bg-slate-800 text-slate-200 text-[14px] md:text-[12px] px-3 py-2 md:px-2 md:py-1 rounded border border-slate-700 min-h-[44px] md:min-h-0 w-full"')

c = c.replace('class="p-1.5 rounded border border-slate-700 bg-[#0f172a] text-slate-200 text-[10px]"', 'class="p-3 md:p-1.5 rounded border border-slate-700 bg-[#0f172a] text-slate-200 text-[14px] md:text-[10px] min-h-[44px] md:min-h-0"')

c = c.replace('class="col-span-2 md:col-span-2 p-1.5 rounded border border-slate-700 bg-[#0f172a] text-slate-200 text-[10px]"', 'class="col-span-1 md:col-span-2 p-3 md:p-1.5 rounded border border-slate-700 bg-[#0f172a] text-slate-200 text-[14px] md:text-[10px] min-h-[44px] md:min-h-0"')

# Buttons
c = c.replace('class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 py-1.5 rounded-md text-[12px] font-bold uppercase tracking-wider transition-colors border border-slate-600"', 'class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-4 py-2 md:px-3 md:py-1.5 rounded-md text-[14px] md:text-[12px] font-bold uppercase tracking-wider transition-colors border border-slate-600 min-h-[44px] md:min-h-0 flex items-center justify-center"')

c = c.replace('class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-1 bg-slate-800 px-3 py-1.5 rounded border border-slate-700"', 'class="text-sm text-slate-400 hover:text-white transition-colors flex items-center gap-2 bg-slate-800 px-4 py-2 md:px-3 md:py-1.5 rounded border border-slate-700 min-h-[44px] md:min-h-0 justify-center"')

c = c.replace('class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-2 py-1 rounded text-[10px] font-bold uppercase tracking-wider transition-colors border border-slate-600 flex items-center gap-1"', 'class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-4 py-2 md:px-2 md:py-1 rounded text-[14px] md:text-[10px] font-bold uppercase tracking-wider transition-colors border border-slate-600 flex items-center justify-center gap-2 min-h-[44px] md:min-h-0"')

# Headings
c = c.replace('class="text-xl font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2"', 'class="text-xl md:text-xl font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2 leading-tight"')

# Ensure body padding is responsive
c = c.replace('class="p-6 max-w-6xl mx-auto min-h-screen flex flex-col"', 'class="p-4 md:p-6 max-w-6xl mx-auto min-h-screen flex flex-col"')

# Table text size
c = c.replace('class="px-2 py-1 text-[9px] text-slate-400 uppercase cursor-pointer"', 'class="px-3 py-2 md:px-2 md:py-1 text-[12px] md:text-[9px] text-slate-400 uppercase cursor-pointer whitespace-nowrap"')
c = c.replace('class="px-2 py-1 text-[9px] text-slate-400 uppercase"', 'class="px-3 py-2 md:px-2 md:py-1 text-[12px] md:text-[9px] text-slate-400 uppercase whitespace-nowrap"')

c = c.replace('class="px-2 py-1 text-[10px] font-mono text-slate-300"', 'class="px-3 py-2 md:px-2 md:py-1 text-[13px] md:text-[10px] font-mono text-slate-300 whitespace-nowrap"')
c = c.replace('class="px-2 py-1 text-[10px] font-bold ${actionColor} uppercase"', 'class="px-3 py-2 md:px-2 md:py-1 text-[13px] md:text-[10px] font-bold ${actionColor} uppercase whitespace-nowrap"')
c = c.replace('class="px-2 py-1 text-[10px] text-slate-300"', 'class="px-3 py-2 md:px-2 md:py-1 text-[13px] md:text-[10px] text-slate-300 whitespace-nowrap"')
c = c.replace('class="px-2 py-1 text-[10px] font-mono ${r.action===\'Buy\'?\'text-red-400\':\'text-emerald-400\'}"', 'class="px-3 py-2 md:px-2 md:py-1 text-[13px] md:text-[10px] font-mono ${r.action===\'Buy\'?\'text-red-400\':\'text-emerald-400\'} whitespace-nowrap"')
c = c.replace('class="px-2 py-1 text-[10px]"', 'class="px-3 py-2 md:px-2 md:py-1 text-[13px] md:text-[10px]"')

c = c.replace('class="text-blue-300 hover:text-blue-200 bg-[#0f172a] px-1.5 py-0.5 rounded border border-blue-500/30"', 'class="text-blue-300 hover:text-blue-200 bg-[#0f172a] px-3 py-2 md:px-1.5 md:py-0.5 rounded border border-blue-500/30 flex items-center justify-center min-h-[44px] min-w-[44px] md:min-h-0 md:min-w-0"')

# Grid fixes for filters
c = c.replace('class="filter-controls grid grid-cols-2 md:grid-cols-4 gap-2 mb-4"', 'class="filter-controls grid grid-cols-1 md:grid-cols-4 gap-3 md:gap-2 mb-4"')
c = c.replace('class="grid grid-cols-1 lg:grid-cols-6 gap-3 mb-3 shrink-0"', 'class="grid grid-cols-1 lg:grid-cols-6 gap-4 md:gap-3 mb-3 shrink-0"')

with open('historial-operaciones.html', 'w', encoding='utf-8') as f:
    f.write(c)
