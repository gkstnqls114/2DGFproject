; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{CA1F8508-3254-4746-8669-3EF1DB865AAE}
AppName=MyGameTest
AppVersion=1.5
;AppVerName=MyGameTest 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\MyGameTest
DisableProgramGroupPage=yes
OutputDir=C:\Users\Han\Desktop
OutputBaseFilename=test setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Han\Desktop\2DGFProject\Project\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Han\Desktop\2DGFProject\Project\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\MyGameTest"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\MyGameTest"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,MyGameTest}"; Flags: nowait postinstall skipifsilent

