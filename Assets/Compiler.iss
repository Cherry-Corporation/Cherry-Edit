; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Cherry-Edit"
#define MyAppVersion "1.0"
#define MyAppPublisher "Cherry Inc."
#define MyAppURL "https://github.com/Cherry-Corporation/Cherry-Edit"
#define MyAppExeName "Cherry-Edit.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{A3D0BFD4-DBA5-442D-9D89-7A250A65CD14}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\Cherry-Edit
DisableDirPage=yes
DefaultGroupName=Cherry-Edit
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\andre\Documents\GitHub\Cherry-Edit\dist
OutputBaseFilename=Cherry-Edit-Installer
SetupIconFile=C:\Users\andre\Documents\GitHub\Cherry-Edit\dist\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\andre\Documents\GitHub\Cherry-Edit\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\andre\Documents\GitHub\Cherry-Edit\dist\HELP.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\andre\Documents\GitHub\Cherry-Edit\dist\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\andre\Documents\GitHub\Cherry-Edit\dist\updater.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

