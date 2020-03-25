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
- [ ] Urychlení verifikace školy [Tabulka](https://docs.google.com/spreadsheets/d/1Q5bnXPTSh9lTvxt1PBqwfwXyozlcINBTyuTV8BwWQ80/edit#gid=0)
- [ ] Pokud se mění MX, tak nastavení SPF, DKIM, DMARC
- [ ] Import uživatel [Tabulka](https://docs.google.com/spreadsheets/d/13KQ8Rr4DiBfDqMQPGH998KCLHELN7fUSXXH_l5Z7Hes/copy) pro vytvoření uživatel a csv pro import. Stačí doplnit doménu a jména uživatel.
- [ ] Organizační složky - Učitelé|Žáci|Zaměstnanci
- [ ] Skupiny dle tříd 
- [ ] Nastavení sdílení adresáře
- [ ] Omezení komunikace na doménu u žáků do 13 let
- [ ] Povolení nahrávání a vysílání u Hangouts Meet 
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