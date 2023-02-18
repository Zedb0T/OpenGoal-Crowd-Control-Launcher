import os

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

class EnvFileChecker:
    def __init__(self, path):
        self.path = path
    
    def check_or_create(self):
        dir_path, file_name = os.path.split(self.path)
        env_file_path = os.path.join(dir_path, file_name)
        if not os.path.isfile(env_file_path):
            with open(env_file_path, "w") as env_file:
                #env_file.write("# This is an example .env file\n")
                #env_file.write("VAR1=value1\n")
                #env_file.write("VAR2=value2\n")
                print("Created a new .env file at", env_file_path)
        else:
            print("Found an existing .env file at", env_file_path)
            
    def addENVtwitchSettings(self):
        #Add fields if they do not exist
        env_file_updater = EnvFileUpdater("env/twitch_settings.env")
        env_file_updater.update(["OAUTH"], "oauth:qxbi1u1zx1cdsasfnkldj69i7yo9okk")
        env_file_updater.update(["TARGET_CHANNEL"], "bikegamepro")
        env_file_updater.update(["PREFIX"], "#")
        env_file_updater.update(["CONNECT_MSG"], "Successfully connected to Channel! peepoHappy")
        env_file_updater.update(["PROTECT_SACRIFICE"], "#t")
        env_file_updater.update(["SACRIFICE_DURATION"], "300")