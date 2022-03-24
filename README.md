# Zoll-API

Abfragen von Importzöllen und Wechselkurse

## Zoll Kurse
curl -H 'Host: zoll.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://zoll.de/SiteGlobals/Functions/Kurse/App/KursExport.txt?view=jsonexportkurseZOLLWeb'

## Zoll Waren

### Kategorien
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//kategorien?client=ZUP&lastModifiedDate=2021-08-16T15:45:06Z&view=renderJson%5BApp%5D'
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//kategorien?client=ZUP&view=renderJson%5BApp%5D'

### Produkte
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//produkte?client=ZUP&lastModifiedDate=2021-08-16T15:45:06Z&view=renderJson%5BApp%5D'

### Länder
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: zollundpost/2 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//laender?client=ZUP&lastModifiedDate=2021-08-16T15:45:06Z&view=renderJson%5BApp%5D'

### Produktgruppen
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: ZollApp/56 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//produktgruppen?client=ZUR&lastModifiedDate=2021-08-16T14:55:49Z&view=renderJson%5BApp%5D'

### Produkteinheiten
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: ZollApp/56 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//produkteinheiten?client=ZUR&lastModifiedDate=2021-08-16T14:55:49Z&view=renderJson%5BApp%5D'

### Slider
curl -H 'Host: www.bundesfinanzministerium.de' -H 'Cache-Control: no-cache' -H 'Accept: */*' -H 'User-Agent: ZollApp/56 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://www.bundesfinanzministerium.de/SiteGlobals/Functions/Apps/retrieve//slider?client=ZUR&lastModifiedDate=2021-08-16T14:55:49Z&view=renderJson%5BApp%5D'
