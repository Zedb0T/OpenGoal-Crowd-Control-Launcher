class EnvFileUpdater:
    def __init__(self, env_file_path):
        self.env_file_path = env_file_path
    
    def update(self, variables, init_value):
        # Load environment variables from file
        with open(self.env_file_path, "r") as f:
            env_lines = f.readlines()

        # Get variable names from environment variables file
        existing_vars = set()
        for line in env_lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            var_name, _ = line.split("=", maxsplit=1)
            existing_vars.add(var_name)

        # Update environment variables with new variables
        with open(self.env_file_path, "a") as f:
            for variable in variables:
                if variable not in existing_vars:
                    value = ""
                    if init_value == "#t":
                        value = "t"
                    elif init_value == "#f":
                        value = "f"
                    elif isinstance(init_value, int):
                        value = str(init_value)
                    elif isinstance(init_value, str):
                        value = init_value
                    f.write(f"{variable}={value}\n")