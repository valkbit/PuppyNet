def StartProgram(moduleName: str):
    try:
        module = __import__(f"Modules.{moduleName}", fromlist=["StartModule"])
        module.StartModule()
    except (ImportError, AttributeError) as e:
        print(f"[-] Failed to load module '{moduleName}': {e}")
