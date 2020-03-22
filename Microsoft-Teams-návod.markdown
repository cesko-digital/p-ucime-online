---
layout: page
title: "Microsoft Teams návod"
permalink: /microsoft-teams-návod
---

## Registrace školy do Office365

-   registraci provést přes stránku [www.office365proskoly.cz](http://www.office365proskoly.cz)

-   tlačítko "Začněte zdarma"

![](images/teams/image1.png)

-   pro novou školu vybrat „Ne, chci registrovat…“

![](images/teams/image2.png)

-   vyplnit informace o škole a správci – vyplnit informace IT admin či ředitel/ka školy

![](images/teams/image3.png)

-   vyplnění údajů o administrátorském účtu daného tenantu – vše zatím v doméně onmicrosoft.com

![](images/teams/image4.png)

-   ověření identity pomocí SMS či hovoru, počkat na ověřovací kód

-   po úspěšném ověření poslední stránka registrace (správa pomocí portálu O365 <https://portal.office.com>

![](images/teams/image5.png)

-   dokončení procesu registrace a přesměrování do administrace O365 (<https://portal.office.com/Adminportal>)

## Dokončení registrace konfigurace tenantu

![](images/teams/image6.png)

-   klinutím na Další v průvodci možnosti přiřazení domény školy

![](images/teams/image7.png)

-   vyplnit požadovanou doménu -\> Použít tuto doménu v následujícím kroku je souhrn pro ověření domény – pomocí TXT či MX záznamu

-   po úpravě v DNS můžete čekat a zkoušet tlačítko Ověřit, případně lze ukončit a vrátit se zpět později (můžete ověřit pomocí nslookup zda už je aktualizace na straně DNS provedena)

-   pokud uzavřete dialog bez ověření znovu spuštění Instalace – Domény – vybrat danou doménu – Spustit nastavování

![](images/teams/image8.png)
![](images/teams/image9.png)
![](images/teams/image10.png)

-   po ověření domény v dalším kroku výběr služeb a zobrazení potřebných DNS záznamů

    -   Exchange (vybrat)

    -   Teams a Skype (vybrat)

    -   Intune a MDM (na zvážení)

![](images/teams/image11.png)

-   dané DNS záznamy přidat přes administraci domény, případně je možné stáhnout zónový soubor, jsou tam všechny potřebné záznamy – stačí jen nakopírovat

-   příklad zónového souboru resp. záznamu pro DNS

```
; Zónový soubor pro služby Office 365: připojte prosím do zónového souboru data uvedená níže
@ 3600 IN MX 0 mojeeu-eu.mail.protection.outlook.com.
autodiscover 3600 IN CNAME autodiscover.outlook.com.
sip 3600 IN CNAME sipdir.online.lync.com.
lyncdiscover 3600 IN CNAME webdir.online.lync.com.
@ 3600 IN TXT "v=spf1 include:spf.protection.outlook.com -all"
_sip._tls.mojeeu.eu. 3600 IN SRV 100 1 443 sipdir.online.lync.com.
_sipfederationtls._tcp.mojeeu.eu. 3600 IN SRV 100 1 5061 sipfed.online.lync.com.
```

![](images/teams/image12.png)

-   úspěšné ověření domény školy

![](images/teams/image13.png)

-   doména automatická onmicrosoft.com a doména školy ověřeny a lze je používat pro generování/vytváření uživatelů a skupin (Instalace – Domény)

## Licence kontrola

-   než začnete vytvářet účty překontrolujte, že máte k dispozici licence Education A1 pro zaměstnance školy a žáky (Fakturace – Licence)

![](images/teams/image14.png)

## Správa uživatelů a skupin O365

Nyní je možné provést vytvoření uživatelů (učitelů a žáků), přidělení licencí, kontrola aktivace služeb. Možnosti jak vytvořit uživatelské účty a skupiny

-   ručně pomocí grafického rozhraní

-   pomocí PowerShellu

-   importem pomocí CSV (pouze uživatelé)

-   integrací s ActiveDirectory (AzureAd Connect)

Zde asi nejčastější varianta zakládání účtů do AzureAD pomocí importu CSV.

### Import uživatelů pomocí CSV

V portálu pro správu O365 (<https://admin.microsoft.com/AdminPortal/>) v menu vybrat Uživatelé – Aktivní uživatelé.

![](images/teams/image15.png)

-   import pomocí dialogu Přidat více uživatelů

![](images/teams/image16.png)

-   možnost stažení vzorových CSV (jen hlavička nebo i vzorová data)

![](images/teams/image17.png)

-   pozor při vyplňování, pokud nějaký parametr nepotřebujete, musíte nechat oddělovač

-   jak využít pro identifikaci žáků ve třídách, použit nejlépe parametry Oddělní a Kancelář, identifikace třídy a oboru dle potřeby

-   ukázkový soubor, který obsahuje jen nezbytně nutné informace Funkce – prázdné, Oddělení – třída, Kancelář – obor/zaměření

![](images/teams/image18.png)

-   v dialogu nahrát soubor CSV a provést ověření správnosti vstupu

![](images/teams/image19.png)

-   dále dle pokynů kliknout na Další

-   v druhém kroku je provedena konfigurace účtů resp. lokalita, povolení přihlášení a přidělení licencí O365 (případně jednotlivých aplikací)

![](images/teams/image20.png)

-   výběrem licence se zobrazí seznam všech aplikací, které je možné ještě jednotlivě vypnout, na zvážení je Yammer ve škole (zjednodušeně školní FB)

![](images/teams/image21.png)

-   stačí klinout na Další, účty se začnou vytvářet o výsledku informuje dialog s možností stažení či zaslání informací o účtech

-   soubor obsahuje Zobrazované jméno, login a heslo

-   výsledkem jsou uživatelé v seznamu

![](images/teams/image22.png)
