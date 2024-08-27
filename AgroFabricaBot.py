import telebot
from telebot import types
import random
import logging

# Initialize the bot with your Telegram API token
API_TOKEN = ' '
bot = telebot.TeleBot(API_TOKEN)

crops = {
    "wheat": {
        "scientific_name": "Triticum aestivum",
        "season": "Winter",
        "climatic_conditions": "Cool, dry climate",
        "properties": "Rich in carbohydrates and proteins",
        "production_rate": "740 million tonnes annually",
        "uses": "Staple food, used in bread, pasta, pastry, etc.",
        "lifespan": "6-8 months",
        "link": 'https://en.wikipedia.org/wiki/Wheat',
        "image_url": 'https://www.world-grain.com/articles/19730-fao-sees-1-increase-in-global-wheat-output'
    },
    "rice": {
        "scientific_name": "Oryza sativa",
        "season": "Summer",
        "climatic_conditions": "Warm, humid climate",
        "properties": "High in carbohydrates, low in fat",
        "production_rate": "500 million tonnes annually",
        "uses": "Staple food, used in various dishes worldwide",
        "lifespan": "4-6 months",
        "link": 'https://en.wikipedia.org/wiki/Rice#:~:text=Rice%20is%20a%20cereal%20grain,glaberrima%20(African%20rice).',
        "image_url": 'https://www.istockphoto.com/photo/ripe-rice-in-the-field-of-farmland-gm622925154-109116633'
    },
    "corn": {
        "scientific_name": "Zea mays",
        "season": "Spring",
        "climatic_conditions": "Warm climate, well-drained soil",
        "properties": "Rich in carbohydrates, fiber, and vitamins",
        "production_rate": "1.1 billion tonnes annually",
        "uses": "Food, animal feed, biofuel, and industrial products",
        "lifespan": "4-6 months",
        "link": 'https://en.wikipedia.org/wiki/Maize',
        "image_url": 'https://www.vecteezy.com/photo/39054665-ai-generated-an-image-of-corn-growing-in-a-corn-field'
    },
    "soybean": {
        "scientific_name": "Glycine max",
        "season": "Summer",
        "climatic_conditions": "Warm climate, fertile and well-drained soil",
        "properties": "High in protein, contains essential amino acids",
        "production_rate": "360 million tonnes annually",
        "uses": "Food products, animal feed, oil production, biofuel",
        "lifespan": "4-5 months",
        "link": 'https://en.wikipedia.org/wiki/Soybean',
        "image_url": 'https://www.britannica.com/plant/soybean'
    },
    "barley": {
        "scientific_name": "Hordeum vulgare",
        "season": "Spring or Winter",
        "climatic_conditions": "Cool climate, tolerant to various soil types",
        "properties": "Rich in fiber, vitamins, and minerals",
        "production_rate": "150 million tonnes annually",
        "uses": "Food, animal feed, brewing, and health products",
        "lifespan": "4-5 months",
        "link": 'https://en.wikipedia.org/wiki/Barley',
        "image_url": 'https://www.indiamart.com/proddetail/barley-7399736830.html'
    },
    "oats": {
        "scientific_name": "Avena sativa",
        "season": "Spring",
        "climatic_conditions": "Cool, moist climate",
        "properties": "High in fiber, protein, and vitamins",
        "production_rate": "25 million tonnes annually",
        "uses": "Food, animal feed, and cosmetic products",
        "lifespan": "4-5 months",
        "link": 'https://en.wikipedia.org/wiki/Oat',
        "image_url": 'https://dengarden.com/agriculture/Oats-Oatmeal-and-Porridge-Plant-Facts-and-Culture'
    },
    "potato": {
        "scientific_name": "Solanum tuberosum",
        "season": "Spring",
        "climatic_conditions": "Cool climate, well-drained and fertile soil",
        "properties": "Rich in carbohydrates, vitamins, and minerals",
        "production_rate": "370 million tonnes annually",
        "uses": "Food, industrial starch, and alcoholic beverages",
        "lifespan": "3-4 months",
        "link": 'https://en.wikipedia.org/wiki/Potato',
        "image_url": 'https://www.isaaa.org/kc/cropbiotechupdate/article/default.asp?ID=18027'
    },
    "sugarcane": {
        "scientific_name": "Saccharum officinarum",
        "season": "Summer",
        "climatic_conditions": "Warm, humid climate",
        "properties": "High in sucrose content",
        "production_rate": "1.9 billion tonnes annually",
        "uses": "Sugar production, biofuel, and alcoholic beverages",
        "lifespan": "10-24 months",
        "link": 'https://en.wikipedia.org/wiki/Sugarcane',
        "image_url": 'https://plantix.net/en/library/crops/sugarcane/'
    },
    "tomato": {
        "scientific_name": "Solanum lycopersicum",
        "season": "Summer",
        "climatic_conditions": "Warm, sunny climate with well-drained soil",
        "properties": "Rich in vitamins, minerals, and antioxidants",
        "production_rate": "180 million tonnes annually",
        "uses": "Food, sauces, soups, and salads",
        "lifespan": "3-5 months",
        "link": 'https://en.wikipedia.org/wiki/Tomato',
        "image_url": 'https://www.vecteezy.com/photo/36212004-ai-generated-fresh-tomato-nature-healthy-green-gourmet-refreshment-generated-by-ai'
    },
    "cotton": {
        "scientific_name": "Gossypium spp.",
        "season": "Summer",
        "climatic_conditions": "Warm climate, well-drained soil",
        "properties": "Natural fiber, high cellulose content",
        "production_rate": "25 million tonnes annually",
        "uses": "Textiles, clothing, and industrial products",
        "lifespan": "5-6 months",
        "link": 'https://en.wikipedia.org/wiki/Cotton',
        "image_url": 'https://www.vecteezy.com/photo/41419555-ai-generated-cotton-field-with-fluffy-white-bolls'
    },
    "peanut": {
        "scientific_name": "Arachis hypogaea",
        "season": "Summer",
        "climatic_conditions": "Warm climate, sandy soil",
        "properties": "High in protein and healthy fats",
        "production_rate": "47 million tonnes annually",
        "uses": "Food, oil production, animal feed",
        "lifespan": "4-5 months",
        "link": 'https://en.wikipedia.org/wiki/Peanut',
        "image_url": 'https://www.irrilinkirrigationequipments.com/crop-information-peanuts-information'
    },
    "avocado": {
        "scientific_name": "Persea americana",
        "season": "Year-round",
        "climatic_conditions": "Tropical and Mediterranean climates",
        "properties": "Rich in healthy fats, vitamins, and minerals",
        "production_rate": "6 million tonnes annually",
        "uses": "Food, oils",
        "lifespan": "10-15 years",
        "link": 'https://en.wikipedia.org/wiki/Avocado',
        "image_url": 'https://www.vecteezy.com/photo/43533598-ripe-avocado-on-the-tree-close-up'
    },
    "blueberries": {
        "scientific_name": "Vaccinium spp.",
        "season": "Summer",
        "climatic_conditions": "Cool, moist climate",
        "properties": "Rich in antioxidants, vitamins, and fiber",
        "production_rate": "0.8 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "20-50 years",
        "link": 'https://en.wikipedia.org/wiki/Blueberry',
        "image_url": 'https://www.frontiersin.org/news/2019/03/14/grass-intercropping-for-sustainable-healthy-blueberry-farming'
    },
    "almonds": {
        "scientific_name": "Prunus dulcis",
        "season": "Autumn",
        "climatic_conditions": "Mediterranean climate",
        "properties": "Rich in healthy fats, protein, and vitamins",
        "production_rate": "2.9 million tonnes annually",
        "uses": "Food, oil production, cosmetics",
        "lifespan": "20-25 years",
        "link": 'https://en.wikipedia.org/wiki/Almond',
        "image_url": 'https://www.thepacker.com/news/produce-crops/despite-challenges-almond-crop-anticipated-weigh-above-2022'
    },
    "quinoa": {
        "scientific_name": "Chenopodium quinoa",
        "season": "Summer",
        "climatic_conditions": "Well-drained soil, cool climate",
        "properties": "Rich in protein, fiber, and essential amino acids",
        "production_rate": "0.2 million tonnes annually",
        "uses": "Food, health products",
        "lifespan": "4-6 months",
        "link": 'https://en.wikipedia.org/wiki/Quinoa',
        "image_url": 'https://www.agrifarming.in/quinoa-farming-information-guide'
    },
    "kiwi": {
        "scientific_name": "Actinidia deliciosa",
        "season": "Autumn",
        "climatic_conditions": "Temperate climate",
        "properties": "Rich in vitamins C and K, fiber",
        "production_rate": "4 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "30-50 years",
        "link": 'https://en.wikipedia.org/wiki/Kiwifruit',
        "image_url": 'https://harvesttotable.com/how-to-plant-grow-prune-and-harvest-kiwifruit/'
    },
    "dragon fruit": {
        "scientific_name": "Hylocereus undatus",
        "season": "Summer",
        "climatic_conditions": "Tropical, subtropical climate",
        "properties": "Rich in antioxidants, vitamins, and fiber",
        "production_rate": "1 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "15-20 years",
        "link": 'https://en.wikipedia.org/wiki/Pitaya',
        "image_url": 'https://www.vecteezy.com/photo/10238258-dragon-fruit-on-the-dragon-fruit-tree-waiting-for-the-harvest-in-the-agriculture-farm-at-asian-pitahaya-plantation-dragon-fruit-in-thailand-in-the-summer'
    },
    "sunflower": {
        "scientific_name": "Helianthus annuus",
        "season": "Summer",
        "climatic_conditions": "Warm, sunny climate",
        "properties": "Rich in oil, vitamins, and minerals",
        "production_rate": "50 million tonnes annually",
        "uses": "Oil production, food, bird feed",
        "lifespan": "3-4 months",
        "link": 'https://en.wikipedia.org/wiki/Sunflower',
        "image_url": 'https://www.agrilearner.com/sunflower-cultivation/'
    },
    "cassava": {
        "scientific_name": "Manihot esculenta",
        "season": "Year-round",
        "climatic_conditions": "Tropical, humid climate",
        "properties": "High in carbohydrates",
        "production_rate": "280 million tonnes annually",
        "uses": "Food, starch production, biofuel",
        "lifespan": "8-18 months",
        "link": 'https://en.wikipedia.org/wiki/Cassava',
        "image_url": 'http://www.kuzabiashara.co.ke/blog/cassava-what-the-growth-of-this-resilient-crop-could-do-for-you-financially/'
    },
    "sorghum": {
        "scientific_name": "Sorghum bicolor",
        "season": "Summer",
        "climatic_conditions": "Warm, dry climate",
        "properties": "Rich in carbohydrates, gluten-free",
        "production_rate": "60 million tonnes annually",
        "uses": "Food, animal feed, biofuel",
        "lifespan": "4-5 months",
        "link": 'https://en.wikipedia.org/wiki/Sorghum',
        "image_url": 'https://sorghumpartners.com/southeastern-united-states-sorghum-production/'
    },
    "millet": {
        "scientific_name": "Panicum miliaceum",
        "season": "Summer",
        "climatic_conditions": "Warm, arid climate",
        "properties": "Rich in fiber, vitamins, and minerals",
        "production_rate": "28 million tonnes annually",
        "uses": "Food, animal feed, brewing",
        "lifespan": "3-4 months",
        "link": 'https://en.wikipedia.org/wiki/Millet',
        "image_url": 'https://www.vecteezy.com/photo/24147651-raw-ripe-millet-crops-in-the-field'
    },
    "coffee": {
        "scientific_name": "Coffea spp.",
        "season": "Year-round (varies by region)",
        "climatic_conditions": "Tropical, high-altitude regions",
        "properties": "Contains caffeine, antioxidants",
        "production_rate": "10 million tonnes annually",
        "uses": "Beverages",
        "lifespan": "20-30 years",
        "link": 'https://en.wikipedia.org/wiki/Coffee',
        "image_url": 'https://www.vecteezy.com/photo/41321822-fresh-coffee-beans-are-on-the-trees-at-the-farm-ready-for-harves'
    },
    "cocoa": {
        "scientific_name": "Theobroma cacao",
        "season": "Year-round",
        "climatic_conditions": "Tropical, humid climate",
        "properties": "Rich in flavonoids, caffeine",
        "production_rate": "5 million tonnes annually",
        "uses": "Chocolate, beverages",
        "lifespan": "25-30 years",
        "link": 'https://en.wikipedia.org/wiki/Cocoa_bean',
        "image_url": 'https://www.vecteezy.com/photo/41760431-ai-generated-cluster-of-flowers-hanging-from-tree-branches'
    },
    "tea": {
        "scientific_name": "Camellia sinensis",
        "season": "Year-round",
        "climatic_conditions": "Tropical and subtropical climates",
        "properties": "Contains caffeine, antioxidants",
        "production_rate": "6 million tonnes annually",
        "uses": "Beverages",
        "lifespan": "30-50 years",
        "link": 'https://en.wikipedia.org/wiki/Tea',
        "image_url": 'https://www.vecteezy.com/photo/37813975-ai-generated-green-fields-under-blue-sky-landscape'
    },
    "banana": {
        "scientific_name": "Musa spp.",
        "season": "Year-round",
        "climatic_conditions": "Tropical, humid climate",
        "properties": "Rich in potassium, vitamins, and fiber",
        "production_rate": "150 million tonnes annually",
        "uses": "Food",
        "lifespan": "9-12 months",
        "link": 'https://en.wikipedia.org/wiki/Banana',
        "image_url": 'https://www.istockphoto.com/photo/banana-tree-gm471467855-21504158'
    },
    "apple": {
        "scientific_name": "Malus domestica",
        "season": "Autumn",
        "climatic_conditions": "Temperate climate",
        "properties": "Rich in fiber, vitamins, and antioxidants",
        "production_rate": "85 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "20-30 years",
        "link": 'https://en.wikipedia.org/wiki/Apple',
        "image_url": 'https://usapple.org/news-resources/apple-production-exports-up-for-2019-crop-says-usapple'
    },
    "grapes": {
        "scientific_name": "Vitis vinifera",
        "season": "Autumn",
        "climatic_conditions": "Temperate, Mediterranean climate",
        "properties": "Rich in vitamins, minerals, and antioxidants",
        "production_rate": "77 million tonnes annually",
        "uses": "Food, wine production, raisins",
        "lifespan": "20-30 years",
        "link": 'https://en.wikipedia.org/wiki/Grape',
        "image_url": 'https://plantix.net/en/library/crops/grape/'
    },
    "orange": {
        "scientific_name": "Citrus sinensis",
        "season": "Winter",
        "climatic_conditions": "Subtropical to tropical climate",
        "properties": "High in vitamin C, antioxidants",
        "production_rate": "75 million tonnes annually",
        "uses": "Food, beverages, flavoring",
        "lifespan": "30-50 years",
        "link": 'https://en.wikipedia.org/wiki/Orange_(fruit)',
        "image_url": 'https://citrusindustry.net/2021/05/27/2021-22-orange-crop-forecast-up-for-brazil/'
    },
    "mango": {
        "scientific_name": "Mangifera indica",
        "season": "Summer",
        "climatic_conditions": "Tropical, subtropical climate",
        "properties": "Rich in vitamins A and C, fiber",
        "production_rate": "50 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "20-30 years",
        "link": 'https://en.wikipedia.org/wiki/Mango',
        "image_url": 'https://www.linkedin.com/pulse/mango-pre-crop-report-2022-abc-fruits'
    },
    "pineapple": {
        "scientific_name": "Ananas comosus",
        "season": "Year-round",
        "climatic_conditions": "Tropical, subtropical climate",
        "properties": "Rich in vitamins, enzymes, antioxidants",
        "production_rate": "28 million tonnes annually",
        "uses": "Food, beverages, desserts",
        "lifespan": "20-24 months",
        "link": 'https://en.wikipedia.org/wiki/Pineapple',
        "image_url": 'https://www.gardeningknowhow.com/edible/fruits/pineapples/care-of-pineapple-plants.htm'
    }
}

# Define a dictionary of fabric types and their descriptions
fabric_types = {
    "cotton": {
        "scientific_name": "Gossypium spp.",
        "intro": "Cotton is a soft, fluffy staple fiber that grows in a boll around the seeds of cotton plants.",
        "uses": "Textiles, clothing, and industrial products",
        "properties": "Soft, breathable, absorbent",
        "link": 'https://tissura.com/articles/cotton-fabrics#:~:text=Cotton%20fabric%20is%20a%20type,around%20us%20for%20many%20centuries.'
    },
    "silk": {
        "scientific_name": "Bombyx mori (Mulberry silk)",
        "intro": "Silk is a natural protein fiber, some forms of which can be woven into textiles. It is produced by certain insect larvae to form cocoons.",
        "uses": "Luxury textiles, clothing, and fine fabrics",
        "properties": "Luxurious, smooth, strong",
        "link": 'https://recovo.co/en/blog/article/what-is-silk-and-how-is-it-made-everything-you-need-to-know'
    },
    "wool": {
        "scientific_name": "Ovis aries (Sheep's wool)",
        "intro": "Wool is the textile fiber obtained from sheep and other animals, including cashmere and mohair from goats, and more.",
        "uses": "Textiles, clothing, carpets, and insulation",
        "properties": "Warm, durable, elastic",
        "link": 'https://en.wikipedia.org/wiki/Wool#:~:text=Wool%20is%20the%20textile%20fiber,properties%20similar%20to%20animal%20wool.'
    },
    "linen": {
        "scientific_name": "Linum usitatissimum (Flax)",
        "intro": "Linen is a textile made from the fibers of the flax plant. Linen is very strong and absorbent, and dries faster than cotton.",
        "uses": "Bedding, clothing, table linen, and upholstery",
        "properties": "Strong, absorbent, dries quickly",
        "link": 'https://en.wikipedia.org/wiki/Linen'
    },
    "polyester": {
        "scientific_name": "Polyethylene terephthalate (PET)",
        "intro": "Polyester is a synthetic fiber derived from coal, air, water, and petroleum. It is durable and resistant to shrinking and stretching.",
        "uses": "Clothing, upholstery, carpets, and industrial applications",
        "properties": "Strong, absorbent, dries quickly",
        "link": 'https://en.wikipedia.org/wiki/Polyester'
    },
    "rayon": {
        "scientific_name": "Rayon (Regenerated cellulose fiber)",
        "intro": "Rayon is a versatile fiber that is made from regenerated cellulose. It can imitate the feel and texture of natural fibers such as silk, wool, cotton, and linen.",
        "uses": "Clothing, medical supplies, and industrial products",
        "properties": "Soft, absorbent, breathable",
        "link": 'https://en.wikipedia.org/wiki/Rayon'
    },
    "nylon": {
        "scientific_name": "Nylon (Polyamide fiber)",
        "intro": "Nylon is a synthetic fiber made from petroleum products. It is known for its high strength and elasticity.",
        "uses": "Clothing, carpets, ropes, and industrial applications",
        "properties": "Strong, elastic, durable",
        "link": 'https://en.wikipedia.org/wiki/Nylon'
    },
    "viscose": {
        "scientific_name": "Viscose (Rayon)",
        "intro": "Viscose is a type of rayon fiber that is made from natural sources such as wood and agricultural products.",
        "uses": "Clothing, upholstery, and packaging",
        "properties": "Soft, breathable, drapable",
        "link": 'https://sewport.com/fabrics-directory/viscose-fabric'
    },
    "cashmere": {
        "scientific_name": "Cashmere wool",
        "intro": "Cashmere wool comes from the cashmere goat, and is known for its softness and warmth.",
        "uses": "Luxury clothing and textiles",
        "properties": "Soft, warm, lightweight",
        "link": 'https://en.wikipedia.org/wiki/Cashmere_wool'
    },
    "acrylic": {
        "scientific_name": "Acrylic fiber",
        "intro": "Acrylic is a synthetic fiber made from polymers of acrylonitrile. It is lightweight and warm, with wool-like properties.",
        "uses": "Knitwear, outdoor clothing, and upholstery",
        "properties": "Lightweight, warm, durable",
        "link": 'https://en.wikipedia.org/wiki/Acrylic_fiber'
    },
    "denim": {
        "scientific_name": "N/A",
        "intro": "Denim is a sturdy cotton warp-faced textile in which the weft passes under two or more warp threads.",
        "uses": "Jeans, jackets, workwear",
        "properties": "Durable, sturdy, versatile",
        "link": 'https://en.wikipedia.org/wiki/Denim'
    },
    "organza": {
        "scientific_name": "N/A",
        "intro": "Organza is a thin, plain weave, sheer fabric traditionally made from silk. Many modern organzas are woven with synthetic filament fibers such as polyester or nylon.",
        "uses": "Evening wear, bridal wear, decorations",
        "properties": "Sheer, thin, crisp",
        "link": 'https://en.wikipedia.org/wiki/Organza'
    },
    "georgette": {
        "scientific_name": "N/A",
        "intro": "Georgette is a sheer, lightweight, crêpe fabric originally made from silk but now often made from synthetic fibers such as polyester.",
        "uses": "Dresses, blouses, scarves",
        "properties": "Sheer, lightweight, crêpe",
        "link": 'https://en.wikipedia.org/wiki/Georgette_(fabric)'
    },
    "velvet": {
        "scientific_name": "N/A",
        "intro": "Velvet is a type of woven tufted fabric in which the cut threads are evenly distributed, with a short dense pile, giving it a distinctive soft feel.",
        "uses": "Clothing, upholstery, curtains",
        "properties": "Soft, luxurious, dense",
        "link": 'https://en.wikipedia.org/wiki/Velvet'
    },
    "satin": {
        "scientific_name": "N/A",
        "intro": "Satin is a weave that typically has a glossy surface and a dull back. It is made from silk, polyester, or nylon.",
        "uses": "Evening wear, lingerie, bedding",
        "properties": "Glossy, smooth, elegant",
        "link": 'https://en.wikipedia.org/wiki/Satin'
    },
    "bamboo": {
        "scientific_name": "Bambusoideae",
        "intro": "Bamboo fabric is made from bamboo fibers. It is known for being soft, breathable, and eco-friendly.",
        "uses": "Clothing, bedding, towels",
        "properties": "Soft, breathable, eco-friendly",
        "link": 'https://en.wikipedia.org/wiki/Bamboo_textiles'
    },
    "modal": {
        "scientific_name": "Beech tree (Fagus sylvatica)",
        "intro": "Modal is a type of rayon made from beech tree pulp. It is known for being soft, breathable, and durable.",
        "uses": "Clothing, underwear, bedding",
        "properties": "Soft, breathable, durable",
        "link": 'https://en.wikipedia.org/wiki/Modal_(textile)'
    },
    "spandex": {
        "scientific_name": "Polyurethane (PU)",
        "intro": "Spandex, also known as Lycra or elastane, is a synthetic fiber known for its exceptional elasticity.",
        "uses": "Activewear, swimwear, undergarments",
        "properties": "Elastic, strong, lightweight",
        "link": 'https://en.wikipedia.org/wiki/Spandex'
    },
    "chiffon": {
        "scientific_name": "N/A",
        "intro": "Chiffon is a lightweight, sheer fabric with a slightly rough texture. It is made from silk, nylon, or polyester.",
        "uses": "Evening wear, scarves, blouses",
        "properties": "Lightweight, sheer, flowing",
        "link": 'https://en.wikipedia.org/wiki/Chiffon_fabric'
    },
    "tweed": {
        "scientific_name": "N/A",
        "intro": "Tweed is a rough, woolen fabric of a soft, open, flexible texture, resembling cheviot or homespun but more closely woven.",
        "uses": "Suits, jackets, skirts",
        "properties": "Durable, warm, textured",
        "link": 'https://en.wikipedia.org/wiki/Tweed_(cloth)'
    },
    "canvas": {
        "scientific_name": "N/A",
        "intro": "Canvas is a heavy-duty, plain-woven fabric used for making sails, tents, marquees, backpacks, and other items for which sturdiness is required.",
        "uses": "Bags, shoes, tents, sails",
        "properties": "Heavy-duty, sturdy, plain-woven",
        "link": 'https://en.wikipedia.org/wiki/Canvas'
    },
    "microfiber": {
        "scientific_name": "Polyester or Polyamide",
        "intro": "Microfiber is a synthetic fiber finer than one denier or decitex/thread. It is known for being soft, absorbent, and quick-drying.",
        "uses": "Cleaning cloths, activewear, upholstery",
        "properties": "Soft, absorbent, quick-drying",
        "link": 'https://en.wikipedia.org/wiki/Microfiber'
    },
    "flannel": {
        "scientific_name": "N/A",
        "intro": "Flannel is a soft woven fabric, of various fineness. It is usually made from wool or cotton, and slightly milled and raised.",
        "uses": "Shirts, pajamas, bedding",
        "properties": "Soft, warm, comfortable",
        "link": 'https://en.wikipedia.org/wiki/Flannel'
    },
    "tulle": {
        "scientific_name": "N/A",
        "intro": "Tulle is a lightweight, very fine netting, often made from nylon, silk, or rayon.",
        "uses": "Tutus, veils, decorative applications",
        "properties": "Lightweight, fine, netting",
        "link": 'https://en.wikipedia.org/wiki/Tulle_(netting)'
    },
    "jersey": {
        "scientific_name": "N/A",
        "intro": "Jersey is a knit fabric used predominantly for clothing manufacture. It was originally made of wool, but is now made of wool, cotton, and synthetic fibers.",
        "uses": "T-shirts, dresses, sportswear",
        "properties": "Elastic, soft, comfortable",
        "link": 'https://en.wikipedia.org/wiki/Jersey_(fabric)'
    },
    "fleece": {
        "scientific_name": "Polyester fleece",
        "intro": "Fleece is a soft, insulating fabric made from polyester. It is used to make warm clothing and blankets.",
        "uses": "Jackets, blankets, activewear",
        "properties": "Soft, insulating, warm",
        "link": 'https://en.wikipedia.org/wiki/Polar_fleece'
    },
    "lace": {
        "scientific_name": "N/A",
        "intro": "Lace is a delicate fabric made of yarn or thread in an open weblike pattern. It is made by hand or machine.",
        "uses": "Lingerie, bridal wear, trims",
        "properties": "Delicate, open-weave, decorative",
        "link": 'https://en.wikipedia.org/wiki/Lace'
    },
    "suede": {
        "scientific_name": "N/A",
        "intro": "Suede is a type of leather with a napped finish, commonly used for jackets, shoes, and other items.",
        "uses": "Shoes, jackets, accessories",
        "properties": "Soft, napped, durable",
        "link": 'https://en.wikipedia.org/wiki/Suede'
    },
    "corduroy": {
        "scientific_name": "N/A",
        "intro": "Corduroy is a textile with a distinct pattern, a 'cord' or wale. The fabric looks as if it is made from multiple cords laid parallel to each other and then stitched together.",
        "uses": "Pants, jackets, skirts",
        "properties": "Textured, durable, patterned",
        "link": 'https://en.wikipedia.org/wiki/Corduroy'
    }
}

# Configure logging
logging.basicConfig(level=logging.INFO)

# State dictionary to keep track of user state
user_state = {}

# Command to greet users with specific commands
@bot.message_handler(func=lambda message: message.text.lower() in ['hi', 'hello', 'namasthe', 'hey'])
def send_greeting(message):
    if message.chat.id not in user_state:
        user_state[message.chat.id] = 'start'
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Explore Crops')
        itembtn2 = types.KeyboardButton('Explore Fabrics')
        markup.add(itembtn1, itembtn2)
        print(bot.send_message(message.chat.id, "Hey there!😊\nWelcome to AgroFabricaBot!🌱\nYour personal assistant for exploring the world of crops and fabrics.\n\nChoose an option below to explore:", reply_markup=markup))
        logging.info(f"User {message.chat.first_name} started the bot with greeting.")
    else:
        bot.send_message(message.chat.id, "Hello!\nAgroFabricaBot at your service. Choose an option below to explore or To explore specific crops or fabrics, simply type their name (e.g., Wheat, Cotton, silk)")

# Command to respond to the /start command
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in user_state:
        user_state[message.chat.id] = 'start'
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Explore Crops')
        itembtn2 = types.KeyboardButton('Explore Fabrics')
        markup.add(itembtn1, itembtn2)
        print(bot.send_message(message.chat.id, " Hello there!😊\nWelcome to the AgroFabricaBot!🌾🧵 Your Crop and Fabric Info Assistant\n\n"
                                                "Choose an option below to explore:⏬\n", reply_markup=markup))
        logging.info(f"User {message.chat.first_name} started the bot with /start command.")
    else:
        bot.send_message(message.chat.id, "Welcome back!\nLooking for crop or fabric info? AgroFabricaBot is here to help. Choose an option below:")

# Command to respond to "thank you"
@bot.message_handler(func=lambda message: message.text.lower() in ['thank you', 'tq', 'thanks','thankyou'])
def respond_thank_you(message):
    responses = [
        "You're welcome! I'm here to help you discover information about crops and fabrics.\n If you want know about any other crop or fabric, feel free to ask.",
        "Glad I could help! If you need more info, I'm here.",
        "You're welcome! Anytime you need info on crops or fabrics, just reach out.",
        "Happy to assist! Let me know if you want to know more about crops or fabrics."
        ]
    response = random.choice(responses)
    bot.send_message(message.chat.id, response)
    logging.info(f"User {message.chat.first_name} is saying thankyou.")

# Command to provide help information
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Hello! I'm AgroFabricaBot, your go-to source for crop and fabric information\n\n"
        "This bot provides information about different crops and fabrics.\n"
        "You can interact with the bot using the following commands:\n"
        "/start - Show the welcome message and options\n"
        "/help - Show this help message\n"
        "/crops - List of available crops\n"
        "/fabrics - List of available fabrics\n"
        "/random - Get random information about a crop or fabric\n"
        "To explore specific crops or fabrics, simply type their name (e.g., Wheat, Cotton)"
    )
    bot.reply_to(message, help_text)
    logging.info(f"User {message.chat.first_name} used /help command.")

# Command to exit the bot
@bot.message_handler(commands=['exit'])
def exit_bot(message):
    goodbye_text = "Exiting the bot. Goodbye!👋"
    bot.reply_to(message, goodbye_text)
    logging.info(f"User {message.chat.first_name} exited the bot.")
    if message.chat.id in user_state:
        del user_state[message.chat.id]

# Command to list available crops
@bot.message_handler(func=lambda message: message.text == 'Explore Crops')
def list_crops(message):
    user_state[message.chat.id] = 'explore_crops'
    markup = types.ReplyKeyboardMarkup(row_width=2)
    for crop in crops.keys():
        markup.add(types.KeyboardButton(crop.capitalize()))
    itembtn_back = types.KeyboardButton('Back')
    markup.add(itembtn_back)
    response = "List of crops:"
    bot.send_message(message.chat.id, response, reply_markup=markup)
    logging.info(f"User {message.chat.first_name} used explore_crops command.")

# Command to list available fabrics
@bot.message_handler(func=lambda message: message.text == 'Explore Fabrics')
def list_fabrics(message):
    user_state[message.chat.id] = 'explore_fabrics'
    markup = types.ReplyKeyboardMarkup(row_width=2)
    for fabric in fabric_types.keys():
        markup.add(types.KeyboardButton(fabric.capitalize()))
    itembtn_back = types.KeyboardButton('Back')
    markup.add(itembtn_back)
    response = "List of fabrics:"
    bot.send_message(message.chat.id, response, reply_markup=markup)
    logging.info(f"User {message.chat.first_name} used explore_fabrics command.")

# Command to handle back button presses
@bot.message_handler(func=lambda message: message.text == 'Back')
def handle_back(message):
    if message.chat.id in user_state:
        del user_state[message.chat.id]
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Explore Crops')
    itembtn2 = types.KeyboardButton('Explore Fabrics')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Back to main menu. Choose an option below to explore:", reply_markup=markup)
    logging.info(f"User {message.chat.first_name} used back command.")

# Command to list available crops
@bot.message_handler(commands=['crops'])
def list_crops_command(message):
    crop_list = "\n".join([f" {crop.capitalize()}" for crop in crops.keys()])
    response = f"Crops:\n\n{crop_list}"
    bot.reply_to(message, response)
    logging.info(f"User {message.chat.first_name} used /crops command.")

# Command to list available fabrics
@bot.message_handler(commands=['fabrics'])
def list_fabrics_command(message):
    fabric_list = "\n".join([f" {fabric.capitalize()}" for fabric in fabric_types.keys()])
    response = f"Fabrics:\n\n{fabric_list}"
    bot.reply_to(message, response)
    logging.info(f"User {message.chat.first_name} used /fabrics command.")

# Command to get random crop or fabric information
@bot.message_handler(commands=['random'])
def random_info(message):
    random_type = random.choice(['crop', 'fabric'])
    logging.info(f"User {message.chat.first_name} asked about {random_type}.")
    if random_type == 'crop':
        random_crop = random.choice(list(crops.keys()))
        crop_info = crops[random_crop]
        response = (
            f"*📌{random_crop.capitalize()}*\n"
            f"**Scientific Name:** {crop_info['scientific_name']}\n"
            f"**Season:** {crop_info['season']}\n"
            f"**Climatic Conditions:** {crop_info['climatic_conditions']}\n"
            f"**Properties:** {crop_info['properties']}\n"
            f"**Production Rate:** {crop_info['production_rate']}\n"
            f"**Uses:** {crop_info['uses']}\n"
            f"**Lifespan:** {crop_info['lifespan']}\n"
        )
        bot.send_photo(message.chat.id, crop_info['image_url'], caption=response, parse_mode='Markdown')
    else:
        random_fabric = random.choice(list(fabric_types.keys()))
        fabric_info = fabric_types[random_fabric]
        response = (
            f"*📌{random_fabric.capitalize()}*\n"
            f"**Scientific Name:** {fabric_info['scientific_name']}\n"
            f"{fabric_info['intro']}\n"
            f"**Uses:** {fabric_info['uses']}\n"
            f"**Properties:** {fabric_info['properties']}\n"
            f"**For More Information:** {fabric_info['link']}\n"
        )
        bot.send_message(message.chat.id, response, parse_mode='Markdown')


# Function to respond to user messages about crops
@bot.message_handler(func=lambda message: message.text.lower() in crops.keys())
def respond_to_crop(message):
    crop = message.text.lower()
    logging.info(f"User {message.chat.first_name} asked about {crop}.")
    crop_info = crops[crop]
    response = (
        f"<b>📌{crop.capitalize()}</b>\n"
        f"<i>Scientific Name:</i> {crop_info['scientific_name']}\n"
        f"<i>Season:</i> {crop_info['season']}\n"
        f"<i>Climatic Conditions:</i> {crop_info['climatic_conditions']}\n"
        f"<i>Properties:</i> {crop_info['properties']}\n"
        f"<i>Production Rate:</i> {crop_info['production_rate']}\n"
        f"<i>Uses:</i> {crop_info['uses']}\n"
        f"<i>Lifespan:</i> {crop_info['lifespan']}\n"
        f"<i>For More Information:</i> {crop_info['link']}\n"
    )
    bot.send_photo(message.chat.id, crop_info['image_url'], caption=response, parse_mode='HTML')

# Function to respond to user messages about fabrics
@bot.message_handler(func=lambda message: message.text.lower() in fabric_types.keys())
def respond_to_fabric(message):
    fabric = message.text.lower()
    logging.info(f"User {message.chat.first_name} asked about {fabric}.")
    fabric_info = fabric_types[fabric]
    response = (
        f"<b>📌{fabric.capitalize()}</b>\n"
        f"<i>Scientific Name:</i> {fabric_info['scientific_name']}\n"
        f"{fabric_info['intro']}\n"
        f"<i>Uses:</i> {fabric_info['uses']}\n"
        f"<i>Properties:</i> {fabric_info['properties']}\n"
        f"<i>For More Information:</i> {fabric_info['link']}\n"
    )
    bot.send_message(message.chat.id, response, parse_mode='HTML')

# Start polling
bot.polling()