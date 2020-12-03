[<script class="next-head" type="application/ld+json">{
    "@context": "http://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 0,
        "name": "Deportes-Bicicletas",
        "item": "https://www.falabella.com/falabella-cl/category/cat70007/Bicicletas"
      }
     ]
  }</script>, <script class="next-head" type="application/ld+json">{
    "@context": "http://schema.org/",
    "@type": "Product",
    "image":["https://falabella.scene7.com/is/image/Falabella/7183918_1"],
    "description": "Bicicleta M.T.B. 27.5 Alum. Hero 310 17.5"",

    "sku": "7183918",




  "brand": {
      "@type": "Thing",
      "name": "XDS"
    },




  "offers": {
    "@type": "Offer",
    "priceCurrency": "CLP",


    "availability": "https://schema.org/InStock",

      "seller": {
      "@type": "Organization",
      "name": "Falabella"
    },

    "price": "329.990"
  },

    "name": "Bicicleta M.T.B. 27.5 Alum. Hero 310 17.5""
  }</script>]


  dateTimeObj = datetime.now()
  cur = conn.cursor()
  query = 'INSERT INTO RESULTS(RES_SCRAP,RES_DATE_SCRAP) VALUES (?, ?)'
  cur.execute(query,(finalElements.replace(" ",""),dateTimeObj))
  conn.commit()
  return cur.lastrowid   