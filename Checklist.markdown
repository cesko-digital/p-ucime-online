---
layout: page
title: "Checklist"
permalink: /checklist
---

## Onboarding

- [ ] Škola má jasno v technologiích - tedy v těch, které chce nebo musí používat
- [ ] Učitelé mají nástroj na úkoly
- [ ] Učitelé mají nástroj pro online video

## Aftercare

- [ ] Učitelé mohou vytvářet kurzy a zadávat úkoly
- [ ] Všichni žáci ve třídě jsou na palubě
- [ ] GDPR Formuláře a poučení předáno

## G Suite

Úkoly specifické pro G Suite

- [ ] Ověřená doména
- [ ] Urchlení verifikace školy [Tabulka](https://docs.google.com/spreadsheets/d/1Q5bnXPTSh9lTvxt1PBqwfwXyozlcINBTyuTV8BwWQ80/edit#gid=0)
- [ ] ...

## MS Teams 

[Příručka Office 365](https://onedrive.live.com/?authkey=%21AFwHysaXtHjS3Gk&cid=D1EE7CF352204F63&id=D1EE7CF352204F63%2111112&parId=D1EE7CF352204F63%2111105&o=OneUp) od strany 17.

Úkoly specifické pro MS Teams

- [ ] Tenant vytvořen - [www.office365proskoly.cz](http://www.office365proskoly.cz)
- [ ] Verifikovaná škola
- [ ] Verifikované domény domena-skoly.cz a student.domena-skoly.cz
- [ ] Povoleny Teams žákům (POZOR ve starém centru pro správu) - [Postup](https://www.klatovsky.cz/2019/11/jak-si-zapnout-teamsy-i-pro-studenty.html)
- [ ] Vytvořeny účty pro učitele a žáky importem CSV ze školní matriky - [Vzorové CSV](https://admin.microsoft.com/UserManagement/Samples/Import_User_Sample_cs.csv)
- [ ] Přiřazeny licence
- [ ] Vytvořeny týmy podle tříd (třída = tým, předmět = kanál)
- [ ] Žáci zařazeni do týmů (např. Powershellem podle CSV)

### Vzor scriptu pro zařazení žáků do tříd
Pro zařazení žáků do tříd je použito stejné CSV jako pro import žáku do Office 365. Pro určení třídy/týmu je použit sloupec "Oddělení" (text musí odpovídat názvu týmu).
```powershell
# Připojení k Azure AD
Import-Module AzureAD # Instalace modulu: Install-Module AzureAD
$cred = Get-Credential
Connect-AzureAD -Credential $cred

# Zařazení žáků do týmů
$users = Import-CSV "Import_User_Template_cs.csv"
Foreach ($user in $users) { 
    $userUPN=$user."Uživatelské jméno"
    $groupName=$user.Oddělení
    Add-AzureADGroupMember -RefObjectId (Get-AzureADUser -All:$True | Where { $_.UserPrincipalName -eq $userUPN }).ObjectID -ObjectId (Get-AzureADGroup | Where { $_.DisplayName -eq $groupName }).ObjectID
}
```