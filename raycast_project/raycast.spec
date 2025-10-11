# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['raycast.py'],
    pathex=[],
    binaries=[],
    datas=[('metal1.mp3', '.'), ('metal2.mp3', '.'), ('test1.mp3', '.'), ('wood1.mp3', '.'), ('step2.mp3', '.'), ('step3.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='raycast',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
