from kivy_deps import sdl2,glew
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calc.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

a.datas +=[('code\calc.kv','C:\\Users\\lenovo\\Desktop\\Python_course_gptl\\kivygui\\calc\calc.kv','DATA')]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='calc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,Tree('C:\\Users\\lenovo\\Desktop\\Python_course_gptl\\kivygui\\calc'),
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins+glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='calc',
)
