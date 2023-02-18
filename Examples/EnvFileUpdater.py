import os
from pathlib import Path

og_dir = os.path.join(os.getenv("APPDATA"), "OpenGOAL-CrowdControl","")

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
        appdata_dir = os.getenv("APPDATA")
        og_dir = os.path.join(appdata_dir, "OpenGOAL-CrowdControl")
        Path(og_dir).mkdir(parents=True, exist_ok=True)
        env_file_path = os.path.join(og_dir, self.path)

        dir_path = os.path.dirname(env_file_path)
        os.makedirs(dir_path, exist_ok=True)

        if not os.path.isfile(env_file_path):
            with open(env_file_path, "w") as env_file:
                print("Created a new .env file at", env_file_path)
        else:
            print("Found an existing .env file at", env_file_path)




    def addENVtwitchSettings(self):
        #Add fields if they do not exist
        env_file_updater = EnvFileUpdater(og_dir + "env/twitch_settings.env")
        env_file_updater.update(["OAUTH"], "oauth:qxbi1u1zx1cdsasfnkldj69i7yo9okk")
        env_file_updater.update(["TARGET_CHANNEL"], "bikegamepro")
        env_file_updater.update(["PREFIX"], "#")
        env_file_updater.update(["CONNECT_MSG"], "Successfully connected to Channel! peepoHappy")
        env_file_updater.update(["PROTECT_SACRIFICE"], "#t")
        env_file_updater.update(["SACRIFICE_DURATION"], "300")

    def addENVcommandDurations(self):
    # Add fields if they do not exist
        env_file_updater = EnvFileUpdater(og_dir + "env/command_durations.env")
        env_file_updater.update(["ACTIVATE_MSG"], "#t")
        env_file_updater.update(["protect_dur"], "60")
        env_file_updater.update(["superjump_dur"], "60")
        env_file_updater.update(["noboosteds_dur"], "180")
        env_file_updater.update(["superboosted_dur"], "180")
        env_file_updater.update(["fastjak_dur"], "90")
        env_file_updater.update(["slowjak_dur"], "45")
        env_file_updater.update(["slippery_dur"], "75")
        env_file_updater.update(["pacifist_dur"], "60")
        env_file_updater.update(["shortfall_dur"], "60")
        env_file_updater.update(["ghostjak_dur"], "3")
        env_file_updater.update(["freecam_dur"], "6")
        env_file_updater.update(["noeco_dur"], "10")
        env_file_updater.update(["rocketman_dur"], "5")
        env_file_updater.update(["invertcam_dur"], "150")
        env_file_updater.update(["dark_dur"], "30")
        env_file_updater.update(["dax_dur"], "300")
        env_file_updater.update(["smallnet_dur"], "10")
        env_file_updater.update(["widefish_dur"], "4")
        env_file_updater.update(["lowpoly_dur"], "300")
        env_file_updater.update(["color_dur"], "90")
        env_file_updater.update(["scale_dur"], "30")
        env_file_updater.update(["widejak_dur"], "45")
        env_file_updater.update(["flatjak_dur"], "45")
        env_file_updater.update(["smalljak_dur"], "45")
        env_file_updater.update(["bigjak_dur"], "45")
        env_file_updater.update(["bighead_dur"], "45")
        env_file_updater.update(["smallhead_dur"], "45")
        env_file_updater.update(["bigfist_dur"], "45")
        env_file_updater.update(["bigheadnpc_dur"], "45")
        env_file_updater.update(["hugehead_dur"], "45")
        env_file_updater.update(["mirror_dur"], "45")
        env_file_updater.update(["notex_dur"], "45")
    
    def addENVcommandEnabled(self):
        #Add fields if they do not exist
        env_file_updater = EnvFileUpdater(og_dir + "env/command_enabled.env")
        env_file_updater.update(["TODO"], "#f")

    def addENVcommandCooldown(self):
        #Add fields if they do not exist
        env_file_updater = EnvFileUpdater(og_dir + "env/command_cooldowns.env")
        env_file_updater.update(["TODO"], "#f")


