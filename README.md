 To get Frank
 Frank is 5.1.1 r9

repo init -u https://github.com/The-Ancile-Project/platform_manifest.git -b frank-mutant-test-1

To Compile

     source build/envsetup.sh

pick a device
     lunch

compile
     make otapackage -j#

-j# means amount of cores plus one so a I7 with 4 cores plus hyperthreading would be 8 cores = -j9 or for max speed


Layers Type 1 is plain RRO from sony
         lollipop fixes
         https://android-review.googlesource.com/#/c/113419/
         https://android-review.googlesource.com/#/c/113650/
         https://android-review.googlesource.com/#/c/113652/
         https://android-review.googlesource.com/#/c/113651/
         https://android-review.googlesource.com/#/c/113653/
         
         newly added fix from sony 8/1/15
         to fix overlay sorting
         https://android-review.googlesource.com/#/c/143049/

Type 2 was the initial to add more things to expand theming. no longer in use

Type 2.1 is current lollipop and was done by Andrew Dodd of Omni to fix a few issues along with renaming the resources to match cmte to make easier porting
commits for 2.1
Written by Branden M and updated for Frank by syko

  platform_frameworks_base commits

    Initial commit to get layers working properly.
    
    https://github.com/The-Ancile-Project/platform_frameworks_base/commit/0e9cbbc63d22093596cb7df770d15f303cd49750


  platform_packages_apps_settings

    Initial exposure of Settings app utilizing layers tag “exposed”.
    
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/6cc6357ad2df115704d16f2243fca8e21ce2546b


   platform_packages_apps_InCallUI

    Exposing InCallUI card backgrounds and utilizing layers tag “exposed”.
     https://github.com/The-Ancile-Project/platform_packages_apps_InCallUI/commit/bfa2c851fd88f371d0717fbf05835f5c8da85664
    
   platform_packages_apps_contacts

    Exposing Contacts header background and text colors. 
    https://github.com/The-Ancile-Project/platform_packages_apps_contacts/commit/dc96c05df54a883f46461e3a514693c175337649
    
   platform_packages_apps_Dialer
   
    Exposing hard coded items within the Dialer.apk
    https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/20d9b74000943b807584d68e34341ca6af495d35
   
   platform_packages_apps_ContactsCommon

    Exposing Contacts more by getting rid of hardcoded codes.
    https://github.com/The-Ancile-Project/platform_packages_apps_ContactsCommon/commit/0fb415861c5c71555d61a23e1f04153e096980b2
    
Layers Type 3

   platform_packages_apps_settings
    
    Fix subsettings force close with some ROMs not utilizing this feature it would conflict with some themes and cause force close in settings.(Cataclysm was the main reason for this).
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/f008fbc107fac2b4d983bc601a20dada8ee2b1d5
    
    Convert Setting Icons to vectors
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/de788db15e5b866303c73c783acaee8565ff5515
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/17087235b9b1c0d5c4c22562b7e82d1c4d9e74fe
       
    Exposing dashboard category backgrounds and dashboard background allowing themers to theme these backgrounds with a: .png, .xml, or still use existing color code while not impacting stock or existing themes. 
    INFO:  https://plus.google.com/u/0/101729058057775926785/posts/XzhYADKHL8Z
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/0f6e58b5e1d66f075dbf8a27b10a77e2ef94ef3f
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/cb26255126b4f3fa30335aaa8cb89ec87a3412ce
    
    No icon left behind for vectors
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/ef8151adc118e03f17533fb956dadebc1e0b9766
    
packages_apps_dialer

    There was a phone icon located on call_log after making a call that was always tinted and has always frustrated us themers due to us not being able to make it a solid color.. So I exposed it by deleting the “0.3” tint to enable us to theme with a solid color or tint like we use to with just the color in res/values/colors.xml 
    INFO: https://plus.google.com/u/0/101729058057775926785/posts

     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/cc03d70b6c5460b1ed06ecf16825a4340139b8db
     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/314f46d02e75ca4d858065d0f8068fa630503cb6
     https://github.com/The-Ancile-Project/platform_packages_apps_Dialer/commit/243db9a1c7c8fa6da47545f448b96af50e123e67
     
 platform_frameworks_base commits
    Allow prevention of doze notification color inversion Doze 2.1
    https://github.com/The-Ancile-Project/platform_frameworks_base/commit/75229c5c4c17bc7fb8cc24f11e1e388756ebf0d7
    
New commits for type 3 8/5/15
    
    Expand on the original settings commit to expose dashboard categories 
    https://github.com/The-Ancile-Project/platform_packages_apps_settings/commit/4b668f02e40a42e1c01d17fc27da9e8331680c8f
    
    