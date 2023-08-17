import importlib

def main():
    module_name = input("Module: ")
    
    try:
        module = importlib.import_module(module_name)
        help(module)
    except ImportError:
        print(f"Module '{module_name}' not found")

if __name__ == "__main__":
    main()
