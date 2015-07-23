 To get Frank
 Frank is 5.1.1 r5

repo init -u https://github.com/The-Ancile-Project/platform_manifest.git -b frank-mutant-test-1

To Compile

     source build/envsetup.sh

pick a device
     lunch

compile
     make otapackage -j#

-j# means amount of cores plus one so a I7 with 4 cores plus hyperthreading would be 8 cores = -j9 or for max speed


Layers Type 1 is plain RRO from sony

Type 2 was the initial to add more things to expand theming. no longer in use

Type 2.1 is current lollipop and was done by Andrew Dodd of Omni to fix a few issues along with renaming the resources to match cmte to make easier porting
commits for 2.1
Written by Branden M and updated for Frank by syko

  platform_frameworks_base commits

    Initial commit to get layers working properly.
    
    https://github.com/The-Ancile-Project/platform_frameworks_base/commit/b38505f4ee5bba79ddbfebabefb090955d76b773


  platform_packages_apps_settings

   Initial exposure of Settings.ap utilizing layers tag “exposed”.
    
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/77481f590a69fd0ce7925497c64a53dca697fc35


   platform_packages_apps_InCallUI

    Exposing InCallUI card backgrounds and utilizing layers tag “exposed”.
     https://github.com/LayersTeam/platform_packages_apps_InCallUI/commit/4af8219e3344ca07052215298f6eff2b879bb62d
    
   platform_packages_apps_contacts

    Exposing Contacts header background and text colors. 
    https://github.com/The-Ancile-Project/platform_packages_apps_contacts/commit/dc96c05df54a883f46461e3a514693c175337649
    
   platform_packages_apps_Dialer
    Exposing hard coded items within the Dialer.apk
    https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/ba7d995a12f696a479612474558996bbddfb66f6
   
   platform_packages_apps_ContactsCommon

    Exposing Contacts more by getting rid of hardcoded codes.
    https://github.com/The-Ancile-Project/platform_packages_apps_ContactsCommon/commit/0fb415861c5c71555d61a23e1f04153e096980b2
    
Recommened Optional commits

   platform_packages_apps_settings
    
    This commit is up to you guys but will help themers color all icons with a simple color code in res/values/colors.xml. I would say about 75% of roms have this commit.
    https://github.com/LayersTeam/platform_packages_apps_settings/commit/f84f50e8e4c96713bed75f49f7fb093f67714f4f

    Fix subsettings force close with some ROMs not utilizing this feature it would conflict with some themes and cause force close in settings.(Cataclysm was the main reason for this).
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/30cf34090be297c3e93ffa1b0141a07912a8bfb6
    
    Convert Setting Icons to vectors
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/e67cd5714196614f7c2f650c4e835f98ef3878e8
       
    Exposing dashboard category backgrounds and dashboard background allowing themers to theme these backgrounds with a: .png, .xml, or still use existing color code while not impacting stock or existing themes. 
    INFO:  https://plus.google.com/u/0/101729058057775926785/posts/XzhYADKHL8Z
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/d82bc73e79cba7d04def1571656d42e972d9aa27
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/966b1edef997ee66d7406a9edf737bc85c9601e7
    
packages_apps_dialer

    There was a phone icon located on call_log after making a call that was always tinted and has always frustrated us themers due to us not being able to make it a solid color.. So I exposed it by deleting the “0.3” tint to enable us to theme with a solid color or tint like we use to with just the color in res/values/colors.xml 
    INFO: https://plus.google.com/u/0/101729058057775926785/posts

     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/cc03d70b6c5460b1ed06ecf16825a4340139b8db
     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/4dde09f1d4d4b229197b6cdbb7a5794f95f6a5e5
     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/8244e9736226f68f2ad8122abb8a90223cd8beec

