try:
    import random
    import time
    import os
    import string
    import fade
    import colorama
    from colorama import Fore
    import socket
    import shutil
    import webbrowser
    import platform
except ModuleNotFoundError:
    os.system("pip install fade")
    os.system("pip install colorama")
    os.system("python optimizyv2.py")

colorama.init(autoreset=True)

#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
#NOT MY TEMP DELETER FILE BC IT WAS 3AM 
# RAAAAAAAAAAAAH

processor = platform.processor()
#i cant set as OS because of import
#could just use OS for this but who cares
if platform.system()!= "Windows":
    print(Fore.RED+"This is a WINDOWS Only program. Please try OPTIMIZY V2 On a windows platform.")
    input(Fore.RED+"Press ENTER To quit...")
    quit()

webbrowser.open("discord.gg/jnn")
webbrowser.open("https://www.youtube.com/channel/UCN8LRd8JnX2FkelKfnfRRfg")

#set all vars
cname = os.getlogin()
desktop_name = socket.gethostname()
version = "V.Beta"
placeholder_alphabet = string.digits + string.ascii_letters
title = fade.fire("""
\t\t\t\t\t     ██╗███╗   ██╗███╗   ██╗
\t\t\t\t\t     ██║████╗  ██║████╗  ██║
\t\t\t\t\t     ██║██╔██╗ ██║██╔██╗ ██║
\t\t\t\t\t██   ██║██║╚██╗██║██║╚██╗██║
\t\t\t\t\t╚█████╔╝██║ ╚████║██║ ╚████║
\t\t\t\t\t ╚════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝
                                                  .gg/jnn
""")
special_thanks = fade.fire("""
\t\t\t\t\t\t   🎆300🎆
\t\t\t\t\t\t   🎆Sub🎆
\t\t\t\t\t         🎆Special🎆
""")
placeholder_table = """
\t\t\t\t\t      ╔═══════════════╗
\t\t\t\t\t      ║ OPTIMIZATIONS ║
\t\t\t\t\t      ╚═══════════════╝
\t\t\t\t\t  //// SYSTEM OPTIMIZERS /////
\t\t\t[1] Internet Commands [2] Clear Temp Files [3] Fix corrupt files
\t\t\t[4] Show system info 

\t\t\t\t\t  //// GAME OPTIMIZERS /////
\t\t\t[5] Fps Unlocker [6] Fortnite Optimizer (OP) [7] Roblox Optimizer (OP)
\t\t\t-----------------------------------------------------------------------
\t\t\t                    [10] ALL OPTIMIZATIONS
\t\t\t-----------------------------------------------------------------------
\t\t\t                      [69] Restart PC
\t\t\tChoose Here:
"""

#TITLE PLACEHOLDER, WHEN PRINT TITLE PRINT: fade.purpleblue(ptitle)
#this line above was old code, do fade IN the title itself.

def loading():
    for x in range(1,5):
        loading_catphrases = (
    "Compiling quantum code snippets",
    "Optimizing multi-threaded logic loops",
    "Initializing neural network connections",
    "Debugging the quantum entanglement protocol",
    "Calibrating cryptographic key matrices",
    "Synchronizing cloud server clusters",
    "Accelerating GPU warp drives",
    "Decrypting the core encryption algorithm",
    "Loading terabytes of cyber-essence",
    "Refactoring nanobot swarm control",
    "Syncing up with interstellar data arrays",
    "Initializing time-traveling algorithms",
    "Defragmenting quantum memory arrays",
    "Syncing up with the metaverse mainframe",
    "Rendering holographic user interfaces",
    "Subscribing to JNN",
    "Joining discord.gg/jnn",
    "Forgetting how to print",
    "Subbing to JNN on youtube",
    "Subscribing to JNN on youtube",
    "Subbing to JNN on youtube",
    "Subscribing to JNN on youtube",
)
        loading_catchprase_randomized = random.choice(loading_catphrases)
        print(fade.random("[Loading] "+loading_catchprase_randomized))
        time.sleep(2)
        os.system("cls")
loading()
print(Fore.GREEN + f"Found OS: {platform.system()}\n" + Fore.GREEN + f"Found Processor: {platform.processor()}\n" + Fore.GREEN + f"Found Machine Network Name: {platform.node()}\n" + Fore.GREEN + f"Found Python Version: {platform.python_version()}\n" + Fore.GREEN + f"Found System Architecture: {platform.architecture()[0]}\n" + Fore.GREEN + f"Found Machine Hardware: {platform.machine()}\n" + Fore.GREEN + f"Found Machine Platform: {platform.platform()}\n" + Fore.GREEN + f"Found Python Implementation: {platform.python_implementation()}\n" + Fore.GREEN + f"Found OS Release Version: {platform.release()}\n" + Fore.GREEN + f"Found OS Version: {platform.version()}")
time.sleep(4)
#Real code
print(title)

def write_settings_to_file(content, path):
    with open(os.path.join(path, 'ClientAppSettings.json'), 'w') as file:
        file.write(content)

def write_fn_to_file(content, path):
    with open(os.path.join(path, 'GameUserSettings.ini'), 'w') as file:
        file.write(content)

def internetopti():
    print("Starting internet optimization now...")
    time.sleep(3)
    os.system("cls")

    print(title)
    os.system("ipconfig /flushdns")
    os.system("cls")
    print(title)
    
    os.system("ipconfig /registerdns")
    os.system("cls")
    print(title)

    os.system("ipconfig /release")
    os.system("cls")
    print(title)

    os.system("ipconfig /renew")
    os.system("cls")
    print(title)

    os.system("netsh winsock reset")
    os.system("cls")
    print(title)
    print(Fore.GREEN+"All done! Going back to main menu...")
    os.system("cls")
    print(title)


#not my temp file deleter
def deletetempfile():
    folder = 'C:/Users/' + os.getlogin() + '/AppData/Local/Temp'
    deleteFileCount = 0
    deleteFolderCount = 0
#not my temp file deleter
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo + 1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print('%s file deleted' % Fore.GREEN + itemName)
                deleteFileCount = deleteFileCount + 1
            elif os.path.isdir(file_path):
                if 'chocolatey' in file_path:
                    continue
                shutil.rmtree(file_path)
                print('%s folder deleted' % itemName)
                deleteFolderCount = deleteFolderCount + 1
        except Exception as e:
            print(Fore.RED + "")
#not my temp file deleter
    print(Fore.GREEN+'Deleting...')
    print(Fore.GREEN + "Deleted ALL deletable temp files!")
    time.sleep(1)
    os.system("cls")
    print(title)

#not my temp file deleter
    

def internetspeedtest():
    print(Fore.GREEN+"Opening Okla Speed Test...")
    webbrowser.open("")#i wanna replace okla because it shows ip and if someone is screensharing its ez doxx
    print(Fore.GREEN+"Opened...")
    time.sleep(3)
    os.system("cls")
    print(title)

def pc_specs():
    #for python version i can just os.system("python -v")
    print(Fore.RED+"Getting CPU Parts")
    processor = platform.processor()
    machine = platform.machine()
    system = platform.system()
    version = platform.version()
    architecture = platform.architecture()
    platform_info = platform.platform()
    python_build = platform.python_build()
    print(Fore.GREEN+"Found machine info!")
    print(f"""
Processor: {processor}
Machine: {machine}
OS: {system}
Version: {version}
Architecture: {architecture}
Platform Info: {platform_info}
Python Build/Version {python_build}
""")
    input(Fore.GREEN+"Press ENTER To go back to main menu...")

def fix_corrupt_file():
    print(Fore.GREEN+"Finding and FIXING Corrupt system files...")
    os.system("sfc /scannow")
    print(Fore.GREEN+"Fixed ALL Corrupted system files.")
    print("Press ENTER To go back to main menu...")
    os.system('cls')

def all_optimizations():
    print(Fore.GREEN+"Starting ALL OPTIMIZATIONS!")
    internetopti()
    deletetempfile()
    fix_corrupt_file()
    fortnite_optimizer()
    ultimate_rbx_fps_boost()
    os.system("cls")
    print(title)
    all_optimizations_restart = input(Fore.RED+"Finished ALL OPTIMIZATIONS! Would you like to restart pc? (Y/N): ")
    if all_optimizations_restart == "y":
        os.system("shutdown /r /f /t 0")
    else:
        pass

def fpsunlocker():

    fps_cap = input("Enter FPS Cap (60-360)")
    fps_unlocker_fflags = """
{
    "DFIntTaskSchedulerTargetFps": """+fps_cap+""",
    "FFlagDebugDisplayFPS": false,
    "FFlagDebugSkyGray": true,
    "FIntCameraFarZPlane": 600
}
"""
    path = input("Please enter ClientAppSettings path: ")
    if os.path.exists(path):
        print(Fore.YELLOW+"Checking path...")
        time.sleep(0.3)
        print(Fore.GREEN+"Path exists!")
    else:
        print(Fore.RED+"Invalid path...")
        input("Press ENTER To go back to main menu...")
    
    if "ClientSettings" in path:
        print(Fore.GREEN+"ClientSettings checked!")
    else:
        print("Invalid ClientSettings but correct path...")
        input("Press ENTER To go back to main menu..")
    write_settings_to_file(fps_unlocker_fflags, path)




def ultimate_rbx_fps_boost():
    path = input("Please enter ClientAppSettings path: ")
    if os.path.exists(path):
        print(Fore.YELLOW+"Checking path...")
        time.sleep(0.3)
        print(Fore.GREEN+"Path exists!")
    else:
        print(Fore.RED+"Invalid path...")
        input("Press ENTER To go back to main menu...")
    
    if "ClientSettings" in path:
        print(Fore.GREEN+"ClientSettings checked!")
    else:
        print("Invalid ClientSettings but correct path...")
        input("Press ENTER To go back to main menu..")

    print("This is BHAGGOS Client App Settings, NOT mine.")
    fps_boost_fflags = """
{
  "FFlagWindowsLaunchAnalytics": "False",
  "DFIntCrashUploadToBacktracePercentage": "0",
  "FFlagRenderGpuTextureCompressor": "True",
  "FFlagEnableSoundTelemetry": "False",
  "FIntReportDeviceInfoRollout": "0",
  "FStringTerrainMaterialTable2022": "",
  "FFlagDisableNewIGMinDUA": "True",
  "FStringPartTexturePackTable2022": "{\u0022foil\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022asphalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022basalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022brick\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022cobblestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022concrete\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022crackedlava\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022diamondplate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022fabric\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glacier\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://98732842556\u0022,\u0022rbxassetid://9438453972\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022granite\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022grass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ground\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ice\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022leafygrass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022limestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022marble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022metal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022mud\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pavement\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pebble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022plastic\u0022:{\u0022ids\u0022:[\u0022\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022rock\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022corrodedmetal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022salt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sand\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sandstone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022slate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022snow\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022wood\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022woodplanks\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]}}",
  "FIntTerrainOTAMaxTextureSize": "1024",
  "DFFlagGpuVsCpuBoundTelemetry": "False",
  "FFlagDebugDisableTelemetryV2Stat": "True",
  "DFFlagESGamePerfMonitorEnabled": "False",
  "FFlagEnableBatteryStateLogger": "False",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL23\u0022": "0",
  "FFlagDebugDisplayFPS": "False",
  "DFFlagQueueDataPingFromSendData": "True",
  "DFFlagEphemeralCounterInfluxReportingEnabled": "False",
  "DFIntUserIdPlayerNameLifetimeSeconds": "86400",
  "FFlagDebugRenderingSetDeterministic": "True",
  "FFlagEnableAudioOutputDevice": "false",
  "FIntHSRClusterSymmetryDistancePercent": "10000",
  "FFlagEnableV3MenuABTest3": "False",
  "FFlagEnableInGameMenuControls": "False",
  "FFlagDebugDisableTelemetryV2Counter": "True",
  "DFIntPredictedOOMPercent": "0",
  "DFStringAltHttpPointsReporterUrl": "null",
  "FIntDefaultMeshCacheSizeMB": "256",
  "DFIntGoogleAnalyticsLoadPlayerHundredth": "0",
  "FFlagNewLightAttenuation": "True",
  "FFlagDebugDisableOTAMaterialTexture": "true",
  "DFLogBatchAssetApiLog": "3",
  "DFIntRunningBaseOrientationP": "450",
  "DFFlagEnableMemProfilingOutsideClient": "False",
  "FFlagFastGPULightCulling3": "True",
  "DFStringLightstepHTTPTransportUrlHost": "null",
  "FFlagRenderPerformanceTelemetry": "False",
  "FFlagEnableMenuModernizationABTest2": "False",
  "DFFlagAvatarChatServiceUserPermissionsAudioEligible": "False",
  "FFlagRenderCheckThreading": "True",
  "FFlagGpuGeometryManager7": "True",
  "FFlagFacialAnimationStreamingServiceUniverseSettingsEnableAudio": "False",
  "DFFlagEnableMemProfilingStorePlaceId": "False",
  "DFIntHttpCurlConnectionCacheSize": "134217728",
  "FFlagVoiceChatServiceManagerUseAvatarChat": "False",
  "DFLogHttpTraceError": "0",
  "DFIntDebugFRMQualityLevelOverride": "1",
  "FFlagHandleAltEnterFullscreenManually": "False",
  "FIntV1MenuLanguageSelectionFeaturePerMillageRollout": "0",
  "DFFlagDebugRenderForceTechnologyVoxel": "True",
  "FFlagAudioDeviceTelemetry": "false",
  "FFlagReportFpsAndGfxQualityPercentiles": "False",
  "DFIntNewRunningBaseAltitudeD": "50",
  "DFFlagCrashUploadFullDumps": "False",
  "DFFlagDebugAnalyticsSendUserId": "False",
  "FintRenderGrassHeightScaler": "0",
  "DFIntLoginTelemetryHundredthsPercent": "0",
  "FStringTerrainMaterialTablePre2022": "",
  "DFIntStartupTracingInfluxRollout": "0",
  "FFlagEnableAdsAPI": "False",
  "FFlagAvatarChatSettingsEnabled2": "False",
  "FIntLinkBrowserTrackerToDeviceRollout": "0",
  "DFFlagEnableFmodErrorsTelemetry": "False",
  "FLogNetwork": "7",
  "FFlagAnimationClipMemCacheEnabled": "True",
  "DFIntClientLightingTechnologyChangedTelemetryHundredthsPercent": "0",
  "FStringErrorUploadToBacktraceBaseUrl": "https://opt-out.roblox.com",
  "FFlagEnableBetaBadgeLearnMore": "false",
  "FFlagFacialAnimationStreamingServiceUserSettingsOptInAudio": "False",
  "FIntBootstrapperTelemetryReportingHundredthsPercentage": "0",
  "DFLogHttpTraceLight": "0",
  "FFlagDebugDisableTelemetryPoint": "True",
  "FIntEmotesAnimationsPerPlayerCacheSize": "16777216",
  "FFlagFixGraphicsQuality": "True",
  "DFIntLightstepHTTPTransportHundredthsPercent2": "0",
  "FFlagPreloadAllFonts": "True",
  "FFlagEnableAccessibilitySettingsEffectsInExperienceChat": "True",
  "FFlagBetaBadgeLearnMoreLinkFormview": "false",
  "FFlagEnableInGameMenuChrome": "true",
  "FFlagDebugDisableTelemetryV2Event": "True",
  "FFlagGraphicsGLEnableSuperHQShadersExclusion": "False",
  "FFlagEnableMenuControlsABTest": "False",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL34\u0022": "0",
  "FFlagCommitToGraphicsQualityFix": "True",
  "FIntCameraMaxZoomDistance": "99999",
  "DFIntCanHideGuiGroupId": "32380007",
  "DFStringLightstepHTTPTransportUrlPath": "null",
  "FFlagEnableInGameMenuChromeABTest": "True",
  "GoogleAnalyticsAccountPropertyIDPlayer": "null",
  "FIntLmsClientRollout2": "0",
  "FStringGamesUrlPath": "/games/",
  "FIntAbuseReportScreenshotMaxSize": "0",
  "DFLogHttpTrace": "0",
  "FFlagEnableMenuModernizationABTest": "False",
  "\u0022FIntCameraMaxZoomDistance\u0022: \u002299999\u0022": "99999",
  "FFlagAvatarChatServiceExposeClientFeaturesForVoiceChat": "False",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistance\u0022": "0",
  "DFStringHttpPointsReporterUrl": "null",
  "DFFlagAddUserIdToSessionTracking": "False",
  "FIntFlagUpdateVersion": "132",
  "FFlagAdServiceEnabled": "False",
  "FFlagDebugDisableTelemetryEventIngest": "True",
  "DFIntBrowserTrackerApiDeviceInitializeRolloutPercentage": "0",
  "FFlagControlBetaBadgeWithGuac": "false",
  "DFFlagEnableHardwareTelemetry": "false",
  "FFlagGlobalWindRendering": "false",
  "DFFlagDisableDPIScale": "True",
  "FFlagNullCheckCloudsRendering": "True",
  "FIntDebugForceMSAASamples": "0",
  "FIntRenderShadowIntensity": "0",
  "DFStringTelemetryV2Url": "null",
  "DFFlagAddPublicGettersForGfxQualityAndFpsForTelemCounters2": "False",
  "FFlagCloudsReflectOnWater": "True",
  "DFFlagClientBaseNetworkMetrics": "False",
  "FIntStartupInfluxHundredthsPercentage": "0",
  "FFlagEnableAccessibilitySettingsInExperienceMenu2": "True",
  "FIntUITextureMaxRenderTextureSize": "1024",
  "DFIntDetectCrashEarlyPercentage": "0",
  "FFlagDebugDisableTelemetryEphemeralCounter": "True",
  "FIntLightingDefaultClearColorARGB": "True;255,255,255,255",
  "DFFlagEnableLightstepReporting2": "False",
  "DFFlagAvatarChatServiceUserPermissionsAudioOptIn": "False",
  "DFFlagHttpCacheCleanBasedOnMemory": "True",
  "FFlagTopBarUseNewBadge": "false",
  "FFlagDontCreatePingJob": "True",
  "FIntRenderLocalLightFadeInMs_enabled": "99999",
  "DFIntTextureQualityOverride": "6",
  "FFlagFacialAnimationStreamingServiceUniverseSettingsEnableVideo": "False",
  "FIntPGSAngularDampingPermillPersecond": "9999999999",
  "\u0022DFIntCSGLevelOfDetailSwitchingDistanceL12\u0022": "0",
  "FFlagTrackWinWebLaunchFlow": "False",
  "FFlagPreloadTextureItemsOption4": "True",
  "GoogleAnalyticsAccountPropertyID": "null",
  "FFlagDebugGraphics": "False",
  "FStringPartTexturePackTablePre2022": "{\u0022foil\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022brick\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022cobblestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022concrete\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022diamondplate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022fabric\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://7547304948\u0022,\u0022rbxassetid://7546645118\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022granite\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022grass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ice\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022marble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022metal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pebble\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022corrodedmetal\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sand\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022slate\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022wood\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022woodplanks\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022asphalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022basalt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022crackedlava\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022glacier\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022ground\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022leafygrass\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022limestone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022mud\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022pavement\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022rock\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022salt\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022sandstone\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]},\u0022snow\u0022:{\u0022ids\u0022:[\u0022rbxassetid://0\u0022,\u0022rbxassetid://0\u0022],\u0022color\u0022:[255, 255, 255, 255]}}",
  "DFIntCSGLevelOfDetailSwitchingDistanceL23": "0",
  "FIntFRMMaxGrassDistance": "0",
  "DFStringAnalyticsNS1BeaconConfig": "https://opt-out.roblox.com",
  "FIntRenderGrassDetailStrands": "0",
  "DFIntCSGLevelOfDetailSwitchingDistanceL12": "0",
  "FFlagGraphicsSettingsOnlyShowValidModes": "True",
  "DFFlagEnableGCapsHardwareTelemetry": "False",
  "DFIntCrashReportingHundredthsPercentage": "0",
  "DFFlagAudioDeviceTelemetry": "False",
  "FFlagCoreGuiTypeSelfViewPresent": "False",
  "DFStringLightstepToken": "null",
  "DFIntWriteFullDmpPercent": "0",
  "FFlagDebugForceFutureIsBrightPhase3": "True",
  "FStringPerformanceSendMeasurementAPISubdomain": "opt-out",
  "DFIntConnectionMTUSize": "900",
  "FFlagLuaAppSystemBar": "False",
  "FIntFRMMinGrassDistance": "0",
  "FFlagGraphicsGLEnableHQShadersExclusion": "False",
  "FIntRenderEnableGlobalInstancingD3D11Percent": "100",
  "FFlagDebugForceChatDisabled": "False",
  "DFStringAnalyticsNS1ApplicationId": "opt-out",
  "FFlagEnableInGameMenuModernization": "False",
  "FFlagEnableAccessibilitySettingsAPIV2": "True",
  "FFlagEnableQuickGameLaunch": "False",
  "DFFlagPredictedOOM": "False",
  "FFlagEnableInGameMenuV3": "False",
  "DFIntCSGLevelOfDetailSwitchingDistance": "1",
  "FStringCoreScriptBacktraceErrorUploadToken": "null",
  "DFStringCrashUploadToBacktraceBaseUrl": "null",
  "DFStringAltTelegrafHTTPTransportUrl": "null",
  "FFlagEnableAccessibilitySettingsEffectsInCoreScripts2": "True",
  "FStringVoiceBetaBadgeLearnMoreLink": "null",
  "FFlagEnableCameraByDefault": "False",
  "FFlagInGameMenuV1FullScreenTitleBar": "False",
  "FFlagVoiceBetaBadge": "false",
  "DFIntCSGLevelOfDetailSwitchingDistanceL34": "0",
  "FFlagBatchAssetApi": "True",
  "FFlagImmersiveAdsWhitelistDisabled": "False",
  "FFlagGraphicsCheckComputeSupport": "True",
  "FIntMeshContentProviderForceCacheSize": "268435456",
  "FFlagDebugGraphicsCrashOnLeaks": "False",
  "FIntRenderShadowmapBias": "0",
  "FFlagDisablePostFx": "True",
  "DFFlagDebugPerfMode": "True",
  "FFlagGraphicsEnableD3D10Compute": "True",
  "DFStringCrashUploadToBacktraceMacPlayerToken": "null",
  "FFlagPreloadMinimalFonts": "True",
  "DFStringCrashUploadToBacktraceWindowsPlayerToken": "null",
  "DFIntUserIdPlayerNameCacheSize": "33554432",
  "FIntFontSizePadding": "3",
  "DFFlagTextureQualityOverrideEnabled": "True",
  "DFStringRobloxAnalyticsURL": "null",
  "DFStringAnalyticsEventStreamUrlEndpoint": "opt-out",
  "FFlagTrackMacWebLaunchFlow": "False",
  "DFFlagVideoCaptureServiceEnabled": "False",
  "DFStringRobloxAnalyticsSubDomain": "opt-out",
  "FFlagFacialAnimationStreamingServiceUserSettingsOptInVideo": "False",
  "FIntTaskSchedulerAutoThreadLimit": "8",
  "DFFlagBrowserTrackerIdTelemetryEnabled": "False",
  "FFlagDebugDisableTelemetryEphemeralStat": "True",
  "DFFlagBaseNetworkMetrics": "False",
  "DFIntS2PhysicsSenderRate": "250",
  "FFlagLocServicePerformanceAnalyticsEnabled": "False",
  "DFStringTelegrafHTTPTransportUrl": "null",
  "FStringImmersiveAdsUniverseWhitelist": "0",
  "FFlagAddGameInstanceIdToSessionTracking": "False",
  "FFlagTrackPlaceIdForCrashEnabled": "False",
  "DFIntTaskSchedulerTargetFps": "120"
}
"""
    write_settings_to_file(fps_boost_fflags,path)#accident put the function instead of the actual clientsettings
    print("Written to ClientAppSettings!")

def fortnite_optimizer():
    game_user_settings = """
[/Script/FortniteGame.FortGameUserSettings]
UnlockConsoleFPS=False
SubGameSelectCount_Athena=313
SubGameLastSelectedTime_Athena=2023.07.06-20.33.52
SubGameSelectCount_Campaign=0
SubGameLastSelectedTime_Campaign=0001.01.01-00.00.00
LastTimeSettingsSnapshotUploaded=2023.07.07-00.33.52
FirstLoginOnDevice=2021.08.29-02.27.37
SafeZone=1.000000
bIsSafeZoneSet=False
CachedPlayerLevel=57
CachedBattleStars=0
CachedAlienStylePoints=0
CachedHighestBattlePassUnlockedPage=5
bShowCareerTabBang=True
CustomVoiceChatInputDevice=
CustomVoiceChatOutputDevice=
CustomVoiceChatInputDeviceId="{30b8e9ce-ab56-45d6-a3ed-ab8f6e033cc4}"
CustomVoiceChatOutputDeviceId=
bMotionBlur=False
bShowGrass=False
bShowFPS=True
bUseGPUCrashDebugging=False
bLatencyTweak1=False
LatencyTweak2=0
bLatencyFlash=False
DLSSQuality=0
bRayTracing=False
ty=True
RayTracingReflectionsQuality=2
RayTracingAmbientOcclusionQuality=False
RayTracingAOQuality=1
RayTracingGIQuality=0
b120FpsMode=False
DisplayGamma=2.700000
UserInterfaceContrast=1.000000
NamedTimes=()
NamedCounts=(("lastfrontendflow_Fortnite", 25),("lastfrontendflow_Fortnite_HotfixVer", 0),("UEnableMultiFactorModal::ShouldShowMFASplashScreen", 24),("UEnableMultiFactorModal::ShouldShowMFASplashScreen_HotfixVer", 0),("FrontendContext:ShouldShowSocialImport", 24),("FrontendContext:ShouldShowSocialImport_HotfixVer", 0),("DiscoveryLobbyMatchmakingPlay", 25),("DiscoveryLobbyMatchmakingPlay_HotfixVer", 0),("Naruto_Cinematic", 18),("Naruto_Cinematic_HotfixVer", 0),("BRUTE_War_Effort", 18),("BRUTE_War_Effort_HotfixVer", 0),("Radish_HypeTrailer", 22),("Radish_HypeTrailer_HotfixVer", 0),("TheKidLaroi_Announce", 23),("TheKidLaroi_Announce_HotfixVer", 0),("Sunburst_Trailer", 23),("Sunburst_Trailer_HotfixVer", 0))
BattlePassOverrideTracker=0
CrewBlingItemShopViolatorUnlockedStagesWhenDisplayed=0
bHasSeenCrewBlingTabBangs=False
bHasSeenDonutShopSequence=False
DonutIdleGameHighScore=0.000000
DisplayAssetPathToOfferSeenLevel=(("v2:/83c2c7dd1240222394ed9c7415fbce183d8504842eebc30039ce96c929d365e6", ItemShopVisited),("v2:/222374fc7ea9f6ef8eb0b3c20f3a5d7f64f612e9f3435c74e3d51d785739bf9f", ItemShopVisited),("v2:/570ff3bed6fc8a1f7006610dbb6ce9e4bcd244a32caa435a60392460da356c88", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MaskedDancer.DAv2_RMT_MaskedDancer", OfferSectionVisited),("v2:/6633ab8087f2a2e80bdf7a90d06351e7a03b82790cc2e286f4b6851020532ed4", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack2800.DA_MtxPack2800", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePass.DA_BR_Season11_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_BattlePass_Tiers25Levels.DAv2_BR_BattlePass_Tiers25Levels", OfferSectionVisited),("v2:/9b91076467e61cf01a3c16e39a18331d2e23d754cdafc860aac0fdd7155615ae", ItemShopVisited),("v2:/83ac0269acedb2d5634a031f55b643b852272903e74d9fa1bb49256a0c06abef", ItemShopVisited),("v2:/aacc97a394a9feaa106ad275caad4e4f22b987d8ceb42d64991024bf6d8a5404", ItemShopVisited),("v2:/4f1c82dc8fb66fef5a0046fb2163344069b65b6ba64e496939d2fc8e8f779157", ItemShopVisited),("v2:/d9fe40e917bf98babee1c239153990efe3e1a568dd0e985c663dbba228eef03f", ItemShopVisited),("v2:/fd2b5edc1839496be18a0cb1ef1bc74c07f391b4448de53d07bb63f695f1763b", ItemShopVisited),("v2:/bfd337ddb7380a663929ae0ad03f6cdbff5b562d1639c8c813cb8316b37f83bb", ItemShopVisited),("v2:/d8c8f59ca26294a0192676567f75ee6c3631f96eea201fd14f8cac0c47acfb5c", ItemShopVisited),("v2:/cb671813542b9346ea26bfb3a53624fee2b73c4d2280c21b37c0bb0759c67574", ItemShopVisited),("v2:/9af32d7a9a16f864eae99d17542ec08763d118f3ce9c72ad05d5fc5f44586dc1", ItemShopVisited),("v2:/8ab132beb750c221f51a79c6b29d10abf9cf7e6a82868226d98abea8add01ac5", ItemShopVisited),("/Game/Items/CardPacks/Events/2021_Anniversary/CardPack_Event_2021_Anniversary.CardPack_Event_2021_Anniversary", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePassWithLevels.DA_BR_Season11_BattlePassWithLevels", ItemShopVisited),("70DBDA11425B10AF7A005D82DB54BC59", ItemShopVisited),("B5FCB8D440CAB93A3080798FACEB77A3", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Subs_CrewBling.DAv2_Subs_CrewBling", OfferSectionVisited),("/Game/Catalog/DisplayAssets/DA_Featured_CID_479_Athena_Commando_F_Davinci.DA_Featured_CID_479_Athena_Commando_F_Davinci", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Jackpot.CardPack_Jackpot", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Basic.CardPack_Basic", ItemShopVisited),("/Game/Items/CardPacks/SpecificRewards/CardPack_Custom_Firecracker_R.CardPack_Custom_Firecracker_R", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Bronze.CardPack_Bronze", ItemShopVisited),("/Game/Items/CardPacks/Events/Persistent_Anniversary/CardPack_Event_Persistent_Anniversary.CardPack_Event_Persistent_Anniversary", ItemShopVisited),("6D971087433F5F475CA2C4B03BA71D6E", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_AnimeLegends_2022.DAv2_RMT_AnimeLegends_2022", OfferSectionVisited),("/Game/Catalog/DisplayAssets/DA_Featured_Nox.DA_Featured_Nox", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_Nox.DAv2_RMT_Nox", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_StatuePose.DAv2_EID_StatuePose", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_PinkJetStarterPack.DAv2_RMT_PinkJetStarterPack", OfferSectionVisited),("/Game/Items/CardPacks/Events/Release/CardPack_Event_Persistent_Lunar.CardPack_Event_Persistent_Lunar", ItemShopVisited),("v2:/28037528dbb0ca0f86fe045cb7c9a909d477ef7f2b58c0dc9345d8bc53f04a9f", ItemShopVisited),("v2:/7bb0f01b723f14330aa6b5e3da5db360ae84eb3f7b54d971b6c0f0b6a366d1d1", ItemShopVisited),("v2:/4a814c8c40f2fac63e29cf51c79c83c0b5427cc42d00352d79e7493958be3ab0", ItemShopVisited),("v2:/371dfc9fe6b6f57e2cc142ca851eb8203ad9bd04ec0cd02a0026b6c6e8d8bf25", ItemShopVisited),("v2:/fdc4d9c5a1a94f2cc9ed8d0317e447267252de646426d80bce54b8a0da17c421", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack13500.DA_MtxPack13500", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack5000.DA_MtxPack5000", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack1000.DA_MtxPack1000", ItemShopVisited),("v2:/cfb51719bd1f2976fe33dfc95890bbc118a3676e5896306f933771fb11b9055c", ItemShopVisited),("v2:/5f489a7fe9b25f51cb04c3fc93c3fef38cb78531cf0b15ac98a9238b18ade989", ItemShopVisited),("v2:/81be4e17ba06b18cae7418dbab3601732356189f14248cd854fcbcad6ac32ce8", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Pickaxe_Basil.DAv2_Pickaxe_Basil", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Wrap_ShinyStar.DAv2_Wrap_ShinyStar", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_492_EmbersMale.DAv2_Pickaxe_ID_492_EmbersMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_SmallFry_KFFA1.DAv2_EID_SmallFry_KFFA1", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_330_M_Keen_2DTXM.DAv2_CID_A_330_M_Keen_2DTXM", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_341_FoeMale_P8JE8.DAv2_Glider_ID_341_FoeMale_P8JE8", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_736_F_DonutDish.DAv2_CID_736_F_DonutDish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_AshtonSaltLake.DAv2_EID_AshtonSaltLake", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_746_F_FuzzyBear.DAv2_CID_746_F_FuzzyBear", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_341_F_Gimmick_RB41V.DAv2_CID_A_341_F_Gimmick_RB41V", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_477_DeliSandwichMale1H.DAv2_Pickaxe_ID_477_DeliSandwichMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_800_UltralightFemale.DAv2_Pickaxe_ID_800_UltralightFemale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_648_StereoFemale_0DTZ9.DAv2_Pickaxe_ID_648_StereoFemale_0DTZ9", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_708_NucleusMale_72W2J.DAv2_Pickaxe_ID_708_NucleusMale_72W2J", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_784_CroissantMale.DAv2_Pickaxe_ID_784_CroissantMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_399_F_Ultralight.DAv2_CID_A_399_F_Ultralight", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_340_M_Gimmick_HK68X.DAv2_CID_A_340_M_Gimmick_HK68X", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_924_M_Embers.DAv2_CID_924_M_Embers", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_BasilStrong.DAv2_Character_BasilStrong", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_ShinyStar.DAv2_Character_ShinyStar", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_745_M_RavenQuill.DAv2_CID_745_M_RavenQuill", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_193_M_Dragonfruit.DAv2_CID_A_193_M_Dragonfruit", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_737_F_DonutPlate.DAv2_CID_737_F_DonutPlate", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_925_F_TapDance.DAv2_CID_925_F_TapDance", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_847_M_Soy_2as3c.DAv2_CID_847_M_Soy_2as3c", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_eid_fireworks_wkx2w.DAv2_eid_fireworks_wkx2w", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_328_M_Foe_S31ZA.DAv2_CID_A_328_M_Foe_S31ZA", OfferSectionVisited),("C0EA93A64B2B3C3F91A0A0B529B5DBE3", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_CupidDarkQuestPack.DAv2_RMT_CupidDarkQuestPack", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_895_M_DeliSandwich.DAv2_CID_895_M_DeliSandwich", OfferSectionVisited),("v2:/b252278bd5ef11b9ef4839a164da24258ffb3587c6ed990a1efa133872a0377e", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_386_M_Croissant.DAv2_CID_A_386_M_Croissant", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_CorruptLegends.DAv2_RMT_CorruptLegends", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_267_M_Nucleus_XVIVU.DAv2_CID_A_267_M_Nucleus_XVIVU", OfferSectionVisited),("v2:/d37cf0f9ff292b537454b920418e48ae8dc3f2bcba9181207e9356a1917f06ec", ItemShopVisited),("v2:/66e127a1f4d6971ec505c030d4ae616ff510c5661b5581a86859219865b8e126", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_EID_Viral.DAv2_EID_Viral", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_400_M_AshtonSaltLake.DAv2_CID_400_M_AshtonSaltLake", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_331_F_Keen_B4LF5.DAv2_CID_A_331_F_Keen_B4LF5", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_033_M_SmallFry_Z73EK.DAv2_CID_A_033_M_SmallFry_Z73EK", OfferSectionVisited),("/Game/Catalog/DisplayAssets/DA_Featured_Wrap_215_CarnavalCycle.DA_Featured_Wrap_215_CarnavalCycle", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_030_CircuitBreaker.DAv2_Glider_ID_030_CircuitBreaker", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_763_F_ShinyJacket.DAv2_CID_763_F_ShinyJacket", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_Elevate.DAv2_Bundle_Featured_Elevate", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_781_F_FuzzyBearTeddy.DAv2_CID_781_F_FuzzyBearTeddy", OfferSectionVisited),("C6BD83734A88D7F0E9B36EBCCE0CCF7C", ItemShopVisited),("v2:/287234268b90b81648c8e860396267c46fa195e77c3b122de0ed0808e1de8583", ItemShopVisited),("v2:/3f1d40299247da6e06f0ced8954c3a8c1219b5372c49aca4126b672645c2dcff", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_Elevate.DAv2_Character_Elevate", OfferSectionVisited),("v2:/913146fea27da376c2e3087bed749db79ac339113be24e190b682e22c7aa8d53", ItemShopVisited),("v2:/5beeba77554d2fb230e99b524a8474c8c2e0831bbaf5e23c54e2af3b6b790682", ItemShopVisited),("v2:/7c98ebcbad6671e8f8aa5feffcddf1df4fa6e3f46887975a015bccf5d55467b6", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Pickaxe_InspireSpell.DAv2_Pickaxe_InspireSpell", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_EID_InspireSpell.DAv2_EID_InspireSpell", OfferSectionVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season24_BattlePass.DA_BR_Season24_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_InspireSpell.DAv2_Character_InspireSpell", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_157_Athena_Commando_F_Stereo_3A08Z.DAv2_CID_A_157_Athena_Commando_F_Stereo_3A08Z", OfferSectionVisited),("v2:/6116c0ba6f4ec41390eebd78d7453fddbb51afa00bedd15fad5ccae50a374e11", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_InspireSpell.DAv2_Bundle_Featured_InspireSpell", OfferSectionVisited),("v2:/2d7313ac43bcbcfcd10adcc82fd774e7d2a60a8075fe19e48d07a5fc8035f319", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_527_Stars.DAv2_Pickaxe_ID_527_Stars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_269_Stars.DAv2_Glider_ID_269_Stars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_732_F_Stars.DAv2_CID_732_F_Stars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_DonutMashup.DAv2_Bundles_DonutMashup", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Gimmick.DAv2_Bundle_Featured_Gimmick", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Keen.DAv2_Bundle_Featured_Keen", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_807_M_CandyApple.DAv2_CID_807_M_CandyApple", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Dragonfruit.DAv2_Bundle_Featured_Dragonfruit", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Foe.DAv2_Bundle_Featured_Foe", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_Donut_Outfits.DAv2_Bundles_Donut_Outfits", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Bundle_Featured_MercurialStorm.DAv2_Bundle_Featured_MercurialStorm", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_AshtonSaltLake_Bundle.DAv2_Bundle_AshtonSaltLake_Bundle", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_730_M_Stars.DAv2_CID_730_M_Stars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_BasilStrong.DAv2_Bundle_Featured_BasilStrong", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_TapDanceBundle.DAv2_Bundles_TapDanceBundle", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Soy.DAv2_Bundle_Soy", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Ultralight.DAv2_Bundle_Featured_Ultralight", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_DeliSandwich.DAv2_Bundles_DeliSandwich", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_Embers.DAv2_Bundles_Embers", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Nucleus.DAv2_Bundle_Featured_Nucleus", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_StereoFemale.DAv2_Bundle_Featured_StereoFemale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_SmallFry.DAv2_Bundle_SmallFry", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Stars.DAv2_Bundle_Featured_Stars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_VMT_ParfaitTriflePack.DAv2_VMT_ParfaitTriflePack", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_PlumCherry.DAv2_RMT_PlumCherry", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Wrap_BlueGlaze.DAv2_Wrap_BlueGlaze", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_820_SpectacleWebMale.DAv2_Pickaxe_ID_820_SpectacleWebMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Featured_SpectacleBundle.DAv2_Featured_SpectacleBundle", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_SpectacleWeb.DAv2_EID_SpectacleWeb", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_430_M_SpectacleWeb.DAv2_CID_A_430_M_SpectacleWeb", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_358_F_Lurk.DAv2_CID_A_358_F_Lurk", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_934_M_Vertigo.DAv2_CID_934_M_Vertigo", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Wrap_DarkAzalea.DAv2_Wrap_DarkAzalea", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Pickaxe_DarkAzalea.DAv2_Pickaxe_DarkAzalea", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Character_DarkAzalea.DAv2_Character_DarkAzalea", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Bundle_Featured_DarkAzalea.DAv2_Bundle_Featured_DarkAzalea", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Pickaxe_BlueGlaze.DAv2_Pickaxe_BlueGlaze", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_BlueGlaze.DAv2_Character_BlueGlaze", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_388_DonutDish1h.DAv2_Pickaxe_ID_388_DonutDish1h", Purchased),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_DesertShadowMale1H.DAv2_Bundle_Featured_DesertShadowMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_664_DragonfruitMale1H_4BIXL.DAv2_Pickaxe_ID_664_DragonfruitMale1H_4BIXL", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_238_Soy_Rwo5d.DAv2_Glider_ID_238_Soy_Rwo5d", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_500_TapDanceFemale1H.DAv2_Pickaxe_ID_500_TapDanceFemale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_BlueGlaze.DAv2_Bundle_Featured_BlueGlaze", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_MusicPack_171_FlailingFins.DAv2_MusicPack_171_FlailingFins", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_074_TeriyakiFishVR.DAv2_Wrap_074_TeriyakiFishVR", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_073_TeriyakiFish2.DAv2_Wrap_073_TeriyakiFish2", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_462_Soy_4cw52.DAv2_Pickaxe_ID_462_Soy_4cw52", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_738_M_DonutCup.DAv2_CID_738_M_DonutCup", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Ultralight.DAv2_EID_Ultralight", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_251_TapDanceFemale.DAv2_Glider_ID_251_TapDanceFemale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_GimmickGear.DAv2_Bundle_Featured_GimmickGear", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_558_SmallFryMale_YBD34.DAv2_Pickaxe_ID_558_SmallFryMale_YBD34", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_250_EmbersMale.DAv2_Glider_ID_250_EmbersMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_EID_BasilStrong.DAv2_EID_BasilStrong", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_245_DeliSandwich.DAv2_Glider_ID_245_DeliSandwich", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_391_Dragonfruit_YVN1M.DAv2_Wrap_391_Dragonfruit_YVN1M", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_343_KeenMale_97P8M.DAv2_Glider_ID_343_KeenMale_97P8M", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_142_AshtonSaltLake.DAv2_Glider_ID_142_AshtonSaltLake", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_306_StereoFemale_0ZZCF.DAv2_Glider_ID_306_StereoFemale_0ZZCF", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_327_NucleusMale_55HFK.DAv2_Glider_ID_327_NucleusMale_55HFK", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_735_FoeMale_2T3KB.DAv2_Pickaxe_ID_735_FoeMale_2T3KB", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_Donut_Accessories1.DAv2_Bundles_Donut_Accessories1", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_072_TeriyakiFish.DAv2_Wrap_072_TeriyakiFish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_142_TeriyakiFish.DAv2_Pickaxe_ID_142_TeriyakiFish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_110_TeriyakiFish.DAv2_Glider_ID_110_TeriyakiFish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_315_M_TeriyakiFish.DAv2_CID_315_M_TeriyakiFish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_XForceGear.DAv2_Bundles_XForceGear", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_736_KeenFemale_3LR4C.DAv2_Pickaxe_ID_736_KeenFemale_3LR4C", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_298_Embers.DAv2_Wrap_298_Embers", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Foe_4EWJV.DAv2_EID_Foe_4EWJV", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_206_Donut.DAv2_Glider_ID_206_Donut", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_203_AshtonSaltLake.DAv2_Pickaxe_ID_203_AshtonSaltLake", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_231_F_Ashes_TKGK9.DAv2_CID_A_231_F_Ashes_TKGK9", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_Backspin.DAv2_Bundles_Backspin", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_749_GimmickMale_5C033.DAv2_Pickaxe_ID_749_GimmickMale_5C033", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_128_M_Menace.DAv2_CID_A_128_M_Menace", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_TeriyakiFish.DAv2_Bundle_Featured_TeriyakiFish", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Wrap_348_Alchemy_FYA4I.DAv2_Wrap_348_Alchemy_FYA4I", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_581_Alchemy_HKAS0.DAv2_Pickaxe_ID_581_Alchemy_HKAS0", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_287_Alchemy_W87KL.DAv2_Glider_ID_287_Alchemy_W87KL", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_349_GimmickMale_MC92O.DAv2_Glider_ID_349_GimmickMale_MC92O", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Ashes_MYQ8O.DAv2_EID_Ashes_MYQ8O", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_737_KeenMale_07J9U.DAv2_Pickaxe_ID_737_KeenMale_07J9U", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_382_Donut1h.DAv2_Pickaxe_ID_382_Donut1h", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_389_DonutPlate1h.DAv2_Pickaxe_ID_389_DonutPlate1h", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_868_M_Backspin_3U6CA.DAv2_CID_868_M_Backspin_3U6CA", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Snap.DAv2_EID_Snap", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Alchemy_BZWS8.DAv2_EID_Alchemy_BZWS8", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Alchemy.DAv2_Bundle_Featured_Alchemy", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_748_GimmickFemale_2W2M2.DAv2_Pickaxe_ID_748_GimmickFemale_2W2M2", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Donut1.DAv2_EID_Donut1", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/EID_Backspin_R3NAI.EID_Backspin_R3NAI", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_446_SeaSalt.DAv2_Pickaxe_ID_446_SeaSalt", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_209_DonutPlate.DAv2_Glider_ID_209_DonutPlate", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_348_GimmickFemale_D76Z0.DAv2_Glider_ID_348_GimmickFemale_D76Z0", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Donut2.DAv2_EID_Donut2", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_241_BackspinMale_97LM4.DAv2_Glider_ID_241_BackspinMale_97LM4", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_387_DonutCup.DAv2_Pickaxe_ID_387_DonutCup", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Gimmick_Male_8ZFCA.DAv2_EID_Gimmick_Male_8ZFCA", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Gimmick_Female_6CMF4.DAv2_EID_Gimmick_Female_6CMF4", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_Season24_BattlePass.DAv2_BR_Season24_BattlePass", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_062_F_Alchemy_XD6GP.DAv2_CID_A_062_F_Alchemy_XD6GP", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/S23/DAv2_EID_FlailingFins.DAv2_EID_FlailingFins", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_834_M_Axl.DAv2_CID_834_M_Axl", Notification),("/Game/Catalog/NewDisplayAssets/S23/DAv2_EID_Chew.DAv2_EID_Chew", Notification),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Bundle_Featured_Sunburst.DAv2_Bundle_Featured_Sunburst", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_454_M_Ohana.DAv2_CID_A_454_M_Ohana", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_042_F_Scholar.DAv2_CID_A_042_F_Scholar", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_340_F_RobotTrouble.DAv2_CID_340_F_RobotTrouble", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_784_F_RenegadeRaiderFire.DAv2_CID_784_F_RenegadeRaiderFire", Notification),("/Game/Catalog/DisplayAssets/DA_Featured_CID_240_Athena_Commando_F_Plague.DA_Featured_CID_240_Athena_Commando_F_Plague", Notification),("/Game/Catalog/NewDisplayAssets/S22/DAv2_Character_DefectBlip.DAv2_Character_DefectBlip", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_864_F_Elastic_E.DAv2_CID_864_F_Elastic_E", Notification),("/Game/Catalog/NewDisplayAssets/S25/DAv2_Character_FauxVenom.DAv2_Character_FauxVenom", Notification),("/Game/Catalog/NewDisplayAssets/DAv2_CID_156_F_FuzzyBearind.DAv2_CID_156_F_FuzzyBearind", Notification),("/Game/Catalog/NewDisplayAssets/S23/DAv2_Character_EmeraldGlassTransform.DAv2_Character_EmeraldGlassTransform", Notification))
LastSelectedPlaylist=(PlaylistName="Playlist_PlaygroundV2",TournamentId="",EventWindowId="",RegionId="NAE",LinkId=(Mnemonic="1832-0431-4852",Version=-1),bGracefullyUpgraded=False,MatchmakingRulePreset=KeepFull)
LastSelectedFillOption=True
bLastSelectedPrivateMatchOption=True
CustomMatchOptions=(("Playlist_BattleLab", (CustomMatchOptions=(("BattleLabMutator_Base:SpawnPortalIndex", "DirtyDocks"),("BattleLabMutator_LootSelection:LootSelection", "Default"),("BattleLabMutator_LootSelection:bUsingExperimentalTables", "True"),("PlaygroundMutator_HeathAndShield:StartingShield", "EmptyShields"),("PlaygroundMutator_HeathAndShield:StartingHealth", "FullHealth"),("PlaygroundMutator_ItemDropOverride:DropAllItemsOverride", "ForceDrop"),("PlaygroundMutator_FallDamage:FallDamageMultiplier", "On"),("PlaygroundMutator_Gravity:GravityOverride", "Normal"),("PlaygroundMutator_TimeOfDay:TimeOfDayOverride", "ForceDay"),("PlaygroundMutator_NamePlates:DisplayMode", "Default")))))
CreativeOptions=(("CreativeOption_EditorCamera", 0),("CreativeOption_Phase", 1),("CreativeOption_FlightSpeed", 1),("CreativeOption_PhoneToolBinding", 1))
bHasSeenCreativePhoneTutorial=False
bHasSeenCreativeHeatmapTutorial=False
CreativeOptionLastUsedCategory=0
CreativeOptionLastUsedIndexInCategory=0
LastNewsVersionViewedBR=
LastNewsVersionViewedCreative=2021-09-11T23:55:57.617Z
LastNewsVersionViewedSTW=
LastPRMEtag=b2492edd0fe1d8d6f85089c54f15f9b8
LastFrontEndBackPlateStageUsed[0]=default
LastFrontEndBackPlateStageUsed[1]=defaultnotris
bEulaAccepted=True
EulaAcceptedUserId=43c9c7e75c704084b2177e59eebaff42
LastEulaCheckTime=2023.07.07-00.33.47
HUDLayoutData[0]=(LayoutEntries=)
HUDLayoutData[1]=(LayoutEntries=)
HUDLayoutData[2]=(LayoutEntries=)
ActiveHUDProfileIdentifier=(HUDProfileType=(TagName=""),Guid=00000000000000000000000000000000)
bTimesSeenBacchusLoadTutorial=0
bHasSeenTapToShoot=False
NumTimesSeeingPanningTip=0
FireModeData=(bAutoFireIsEnabled=True,b3DTouchEnabled=False,bTapToShootEnabled=False,bAlwaysShowDedicatedButton=True,FireModeType=Unset)
SimpleMobileStats=(GamesPlayed=698,SecondsPlayed=87750,KillCount=1650,BestResult=4,LastReviewPromptDay=0001.01.01-00.00.00,CampaignGamesPlayed=0)
AudioOutputDeviceId=
bUseHeadphoneMode=False
InitialBenchmarkState=1
bDisableMouseAcceleration=False
ChosenLoginType=None
SocialImportOptedOutVersion=1
VKImportOptedOutVersion=0
bHasSeenErebusSocialImport=False
bHasSeenFriendImportToast=False
LastSocialImportPromptTime=2021.11.13-20.31.28
bAutoImportFriendEnabled=False
bSeenLetoSellModal=False
SocialImportPromptCountCurrentVersion=4
SocialImportPromptCountAllVersions=4
VKImportPromptCountCurrentVersion=0
VKImportPromptCountAllVersions=0
LastAccountItemWarningTime=0001.01.01-00.00.00
bMultiFactorAuthModalOpOut=False
LastEnableMFAModalPromptTime=0001.01.01-00.00.00
LastVKImportPromptTime=0001.01.01-00.00.00
LastAffiliateToastTime=0001.01.01-00.00.00
FailedInviteMap=()
MobileRecommendationDismissedVersion=0
ShowLiveStreamPictureInPictureInMatchV2=Default
CurrentLivePiPStreamOverrideCounter=0
SelectedFrontEnd=
bNeverShowMobileLink=False
bHasMigratedDownloadSettings=False
bSendAppsFlyerEventOnInstallation=True
bAllowFullGameDownload=False
bAllowCellularDownload=False
bAutoDownloadHighResTextures=False
LastAutoDownloadHighResTextureReminder=638242879369870000
bAutoLaunchFullGame=False
bAllowDownloadHighResMips=True
bAllowLowPowerMode=False
bAllowVideoPlayback=False
bAllowMultithreadedRendering=True
MobileFPSMode=Mode_30Fps
MobileQualitySettingsResetDefaultsGUID=
bHasSeenSamsungPressureSensorWarning=False
bNeverDisplaySamsungPressureSensorWarning=False
bHasRecentlySeenBadMatchPopup=False
MatchesSinceLastBadMatchPopup=0
bHasAlreadyRatedOnGooglePlay=False
DaysToSnoozeBeforeNextGooglePlayRating=0
GooglePlayRatingDelayedOccurences=0
bShowTemperature=False
LastGameStartNotificationSentTime=0001.01.01-00.00.00
LastYearForcedDisplayWinterfestInfoButton=0
bHasSeenSidekickWelcomePopup=False
bPCMigratedToNextGenScalability=True
bUseVSync=False
bUseDynamicResolution=False
ResolutionSizeX=1920
ResolutionSizeY=1080
LastUserConfirmedResolutionSizeX=1920
LastUserConfirmedResolutionSizeY=1080
WindowPosX=-1
WindowPosY=-1
LastConfirmedFullscreenMode=0
PreferredFullscreenMode=0
AudioQualityLevel=1
LastConfirmedAudioQualityLevel=1
FrameRateLimit=0.000000
DesiredScreenWidth=1862
DesiredScreenHeight=1047
LastUserConfirmedDesiredScreenWidth=1862
LastUserConfirmedDesiredScreenHeight=1047
LastRecommendedScreenWidth=-1.000000
LastRecommendedScreenHeight=-1.000000
LastCPUBenchmarkResult=-1.000000
LastGPUBenchmarkResult=-1.000000
LastGPUBenchmarkMultiplier=1.000000
bUseHDRDisplayOutput=False
HDRDisplayOutputNits=1750
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=cd6f8a2156d7453086fc7baf945b6527,EncounterTime=2021.08.29-19.55.08)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=843811163bfb4686a40c60df007056a1,EncounterTime=2021.08.30-19.03.47)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=e834187ab4f74e21992292e75f234f04,EncounterTime=2021.08.31-19.30.53)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=a8b0f2178ac344d89e168c10de25a3b3,EncounterTime=2021.09.01-17.34.19)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=e948b7790a8b4c5d973f107b6ba02229,EncounterTime=2021.09.01-17.34.22)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=4e9e3dd0f5404026a376135e0bc091c1,EncounterTime=2021.09.01-17.58.14)
RecentPlayerEncounters=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,UserId=746ac685b44d465fb5451a30b6fb51d1,EncounterTime=2021.09.07-20.45.57)
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=20eb3e58d7684a6bb4316de3abca4b41,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=9a4ce187fe3a43db8449150f280fba86,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=0c03baeca8d84d0e9753be2c8beffe95,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=ea0ca8d3a0ed46dda92cdd317ba5507a,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=d2ef5dac539b42a7ab6f6c8b35ffaaec,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=2eae78846d12430a91c7a2acd75973f0,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=3c4aeac0510804ea5b07035f5ee0ca814,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=ac2f828596d3400aa08515b1f05a408e,SocialStatus=(AttendingSocialEventIds=(1)))
FriendSocialStatuses=(LocalUserId=e6ad38ee620f4cd0a8087032a9ed5872,OtherUserId=9050bf7ec35a45729e57dccbbfc69d3c,SocialStatus=(AttendingSocialEventIds=(1)))
bShowActorsWithSeasonItemTagMapIndicators=True
CachedStylePoints=0
CachedClaimableRewards=(("Reward", 3),("Weekly", 0),("Bonus", 0))
FrontendQuestTooltipDisplayedCount=0
AutoDownloadHighResTexturesBehavior=Disabled_Permanent
RayTracingShadowsQuality=True
bGoalPagePinTooltipViewed=False
FrontendFrameRateLimit=120
ItemShopSectionsSeenStateLastResetDates=(("Featured", 0001.01.01-00.00.00),("Daily", 0001.01.01-00.00.00),("Featured2", 0001.01.01-00.00.00),("LimitedTime", 0001.01.01-00.00.00),("BattlePass", 2023.03.11-01.44.16),("Subscription", 2023.03.01-01.07.15),("Featured3", 0001.01.01-00.00.00),("Marvel20B", 0001.01.01-00.00.00),("Marvel19B", 0001.01.01-00.00.00),("Marvel18B", 0001.01.01-00.00.00),("Marvel17B", 0001.01.01-00.00.00),("Marvel16B", 0001.01.01-00.00.00),("Marvel15B", 0001.01.01-00.00.00),("Marvel14B", 0001.01.01-00.00.00),("Marvel13B", 0001.01.01-00.00.00),("Marvel4", 0001.01.01-00.00.00),("Marvel12B", 0001.01.01-00.00.00),("Marvel11B", 0001.01.01-00.00.00),("Marvel10B", 0001.01.01-00.00.00),("Marvel9B", 0001.01.01-00.00.00),("CreedB", 0001.01.01-00.00.00),("Marvel8B", 0001.01.01-00.00.00),("Marvel7B", 0001.01.01-00.00.00),("Marvel6B", 0001.01.01-00.00.00),("Marvel5B", 0001.01.01-00.00.00),("Marvel3B", 0001.01.01-00.00.00),("Marvel2B", 0001.01.01-00.00.00),("MarvelB", 0001.01.01-00.00.00),("Marvel0B", 0001.01.01-00.00.00),("HorizonZeroDawnB", 0001.01.01-00.00.00))
ContentQualityLevelSelected=Unset
CurrentLockerSorts=((Pickaxe, Invalid),(Character, Invalid),(Backpack, Invalid))
FortniteReleaseVersion=6
FortAntiAliasingMethod=TAA
TemporalSuperResolutionQuality=Recommended
NewestProgressiveCosmeticSetSeen=
bHasUsedBattlePassCrewUpsellNavButton=False
bHasSeenLockerArchivingCleanupTooltip=True
bHasSeenGeneralArchiveModeTooltip=False
bHasSeenEmotesArchiveModeTooltip=False
bHasSeenArchiveFilterTooltip=False
bHasSeenArchivedItemsTooltip=False
LastSelectedChildActivityMap=()
LastYearWinterfestWasSeen=2022
bHasSeenLobbyModeSetNotification=True
bHasSeenLobbyModeChangedNotification=True
bHasSeenDiscoveryModeSetNotification=True
HasSeenDiscoveryDetailsModeSetNotificationMnemonics=()
LowInputLatencyModeIsEnabled=True
bNeedsToSeeFireModeSelectionReminder=False
MatchesSinceInitialFireModeSelection=0
bHasSeenCreatorPageFirstTimeTooltip=False
bUseNanite=False
DesiredGlobalIlluminationQuality=1
DesiredReflectionQuality=1
PreNaniteGlobalIlluminationQuality=0
PreNaniteReflectionQuality=0
FullscreenMode=0
bHasSeenQuickSaveTooltip=False
CosmeticStreamingEnabled=CodeSet_Enabled
bStopRenderingInBackground=False
bIsEnergySavingEnabledIdle=False
bIsEnergySavingEnabledFocusLoss=False
EnergySavingLevelFocusLoss=1
bHasUserSeenQuickSaveTooltip=False
bHasUserSeenLockerActionBarTooltip=False
bHasSeenDiscoveryCCUModal=True

[ScalabilityGroups]
sg.ResolutionQuality=97
sg.ViewDistanceQuality=0
sg.AntiAliasingQuality=0
sg.ShadowQuality=0
sg.PostProcessQuality=0
sg.TextureQuality=0
sg.EffectsQuality=0
sg.FoliageQuality=0
sg.ShadingQuality=0
sg.GlobalIlluminationQuality=0
sg.ReflectionQuality=0

[ChatSettings]
HideSocialName=False
AutoImportFriends=False
AutoDeclineFriendRequests=True
ShowNotifications=False
NeverFadeMessages=True
ShowTimeStamps=True
ShowWhispersInAllTabs=True
ShowCustomTab=False
ShowWhispersTab=True
ShowGlobalTab=True
ShowCombatAndEventsTab=False
ShowClanTabs=False
HideOffline=False
HideOutgoing=False
HideSuggestions=False
HideRecent=False
HideBlocked=True
FilterMatureLanguage=True
DisplayCharacterNames=False
FriendInviteReceivedCueEnabled=False
GameOrPartyInviteReceivedCueEnabled=True
MessageReceivedCueEnabled=False
SoundEnabled=False
ShowTextChat=True
FontSize=1
WindowHeight=0
WindowOpacity=0.5

[D3DRHIPreference]
PreferredFeatureLevel=es31
PreferredRHI=dx11

[ShaderPipelineCache.CacheFile]
LastOpened=FortniteGame

[PerformanceMode]
MeshQuality=0

[RayTracing]
r.RayTracing.EnableInGame=False


"""
    print(Fore.GREEN+"This Game User Settings is from (kxng)")
    time.sleep(1)
    print("Auto checking for Fortnite Path")
    if os.path.exists("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\FortniteGame\\Saved\\Config\\WindowsClient"):
        print("Automatically found path!")
        real_fn_path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\FortniteGame\\Saved\\Config\\WindowsClient"
        time.sleep(3)
    else:
        while True:
            print(Fore.RED+"Could not automatically find fortnite path.")
            fn_path = input('Enter GameUserSettings path\nFor a tutorial type (T), or else type your path: ').lower()
            if fn_path == "t":
                webbrowser.open("https://www.google.com/search?q=fortnite+game+user+settings+path&rlz=1C1ONGR_enUS1093US1093&oq=fortnite&gs_lcrp=EgZjaHJvbWUqBggAECMYJzIGCAAQIxgnMgYIARBFGDkyDggCEEUYOxhDGIAEGIoFMgYIAxBFGDsyBggEEEUYOzIGCAUQRRg8MgYIBhBFGD0yBggHEEUYPNIBCDI1MTFqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8")
                os.system("cls")
            else:
                real_fn_path = fn_path
                break
            
    if os.path.exists(real_fn_path):
        pass
    else:
        input('Invalid fortnite path. Press ENTER To go back to main menu: ')
    write_fn_to_file(game_user_settings, real_fn_path)
    print("Optimized fortnite!")
    input(Fore.GREEN+"Press ENTER To go back to main menu...")

#CHANGE TITLE

pre_sys_title = string.digits + string.ascii_letters

def ct():
    sys_title = "".join(random.choices(pre_sys_title, k=100))
    os.system(f"title {sys_title}")

while True:
    ct()
    os.system("cls")
    print(special_thanks)
    print(fade.fire(title))
    table = input(fade.fire(placeholder_table))
    if table == "1":
        ct()
        internetopti()
        ct()
    elif table == "2":
        ct()
        deletetempfile()
        ct()
    elif table == "3":
        ct()
        fix_corrupt_file()
        ct()
    elif table == "4":
        ct()
        pc_specs()
        ct()
    elif table == "5":
        ct()
        fpsunlocker()
        ct()
    elif table == "6":
        ct()
        fortnite_optimizer()
        ct()
    elif table == "7":
        ct()
        ultimate_rbx_fps_boost()
        ct()
    elif table == "69":
        os.system("shutdown /r /f /t 0")
    elif table == "10":
        ct()
        all_optimizations()
        ct()
    else:
        for cycle_seconds in reversed(range(1,4)):
            ct()
            print(f"{Fore.RED}Invalid choice.. Going back to main menu in {cycle_seconds} seconds.")
            time.sleep(1)
            os.system("cls")
            print(title)
            ct()
