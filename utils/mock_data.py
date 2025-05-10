clothing_items = [
    {"id": 1, "item_type": "shirt", "color": "red", "material": "cotton", "gender": "male", "style": "casual", "brand": "Uniqlo", "season": "summer", "price": 25, "description": "A comfortable red cotton shirt.", "usage_context": "Everyday casual wear."},
    {"id": 2, "item_type": "pants", "color": "blue", "material": "denim", "gender": "male", "style": "casual", "brand": "Levi's", "season": "all", "price": 50, "description": "Classic blue jeans.", "usage_context": "Casual outings and daily wear."},
    {"id": 3, "item_type": "dress", "color": "black", "material": "silk", "gender": "female", "style": "formal", "brand": "Zara", "season": "summer", "price": 80, "description": "Elegant black silk dress.", "usage_context": "Formal events and parties."},
    {"id": 4, "item_type": "skirt", "color": "white", "material": "linen", "gender": "female", "style": "casual", "brand": "H&M", "season": "summer", "price": 30, "description": "Light white linen skirt.", "usage_context": "Summer outings."},
    {"id": 5, "item_type": "jacket", "color": "green", "material": "leather", "gender": "unisex", "style": "sporty", "brand": "Nike", "season": "fall", "price": 120, "description": "Sporty green leather jacket.", "usage_context": "Outdoor activities."},
    {"id": 6, "item_type": "shirt", "color": "blue", "material": "linen", "gender": "male", "style": "formal", "brand": "Uniqlo", "season": "spring", "price": 35, "description": "Blue linen shirt for formal occasions.", "usage_context": "Office and meetings."},
    {"id": 7, "item_type": "pants", "color": "black", "material": "cotton", "gender": "female", "style": "formal", "brand": "Zara", "season": "all", "price": 45, "description": "Black cotton pants.", "usage_context": "Work and formal events."},
    {"id": 8, "item_type": "dress", "color": "red", "material": "cotton", "gender": "female", "style": "casual", "brand": "H&M", "season": "summer", "price": 40, "description": "Red cotton summer dress.", "usage_context": "Casual summer days."},
    {"id": 9, "item_type": "shoes", "color": "white", "material": "leather", "gender": "female", "style": "casual", "brand": "Adidas", "season": "all", "price": 60, "description": "White leather sneakers.", "usage_context": "Everyday wear."},
    {"id": 10, "item_type": "shoes", "color": "black", "material": "leather", "gender": "male", "style": "formal", "brand": "Clarks", "season": "all", "price": 90, "description": "Black formal leather shoes.", "usage_context": "Business and formal events."},
    {"id": 11, "item_type": "accessories", "color": "silver", "material": "metal", "gender": "female", "style": "formal", "brand": "Pandora", "season": "all", "price": 70, "description": "Elegant silver bracelet.", "usage_context": "Formal occasions."},
    {"id": 12, "item_type": "accessories", "color": "brown", "material": "leather", "gender": "male", "style": "casual", "brand": "Fossil", "season": "all", "price": 40, "description": "Brown leather belt.", "usage_context": "Casual and business casual."},
    {"id": 13, "item_type": "coat", "color": "grey", "material": "wool", "gender": "female", "style": "formal", "brand": "Mango", "season": "winter", "price": 150, "description": "Warm grey wool coat.", "usage_context": "Winter formal events."},
    {"id": 14, "item_type": "scarf", "color": "red", "material": "wool", "gender": "unisex", "style": "casual", "brand": "Gap", "season": "winter", "price": 20, "description": "Red wool scarf.", "usage_context": "Cold weather accessory."},
    {"id": 15, "item_type": "blazer", "color": "navy", "material": "wool", "gender": "male", "style": "formal", "brand": "Boss", "season": "fall", "price": 200, "description": "Navy wool blazer.", "usage_context": "Business meetings and formal events."},
    {"id": 16, "item_type": "shorts", "color": "beige", "material": "cotton", "gender": "male", "style": "casual", "brand": "Old Navy", "season": "summer", "price": 22, "description": "Beige cotton shorts.", "usage_context": "Summer leisure."},
    {"id": 17, "item_type": "t-shirt", "color": "yellow", "material": "cotton", "gender": "female", "style": "casual", "brand": "Zara", "season": "summer", "price": 18, "description": "Bright yellow t-shirt.", "usage_context": "Casual summer days."},
    {"id": 18, "item_type": "boots", "color": "brown", "material": "leather", "gender": "female", "style": "casual", "brand": "Timberland", "season": "fall", "price": 110, "description": "Brown leather boots.", "usage_context": "Outdoor and fall wear."},
    {"id": 19, "item_type": "sweater", "color": "purple", "material": "wool", "gender": "female", "style": "casual", "brand": "H&M", "season": "winter", "price": 35, "description": "Purple wool sweater.", "usage_context": "Winter casual wear."},
    {"id": 20, "item_type": "hat", "color": "black", "material": "felt", "gender": "unisex", "style": "casual", "brand": "Brixton", "season": "fall", "price": 28, "description": "Black felt hat.", "usage_context": "Fashionable fall accessory."},
    {"id": 21, "item_type": "cardigan", "color": "cream", "material": "wool", "gender": "female", "style": "casual", "brand": "Uniqlo", "season": "spring", "price": 32, "description": "Cream wool cardigan.", "usage_context": "Spring layering."},
    {"id": 22, "item_type": "leggings", "color": "black", "material": "spandex", "gender": "female", "style": "sporty", "brand": "Nike", "season": "all", "price": 30, "description": "Black spandex leggings.", "usage_context": "Sport and athleisure."},
    {"id": 23, "item_type": "tank top", "color": "white", "material": "cotton", "gender": "female", "style": "casual", "brand": "H&M", "season": "summer", "price": 12, "description": "White cotton tank top.", "usage_context": "Hot summer days."},
    {"id": 24, "item_type": "sandals", "color": "tan", "material": "leather", "gender": "female", "style": "casual", "brand": "Birkenstock", "season": "summer", "price": 55, "description": "Tan leather sandals.", "usage_context": "Beach and summer outings."},
    {"id": 25, "item_type": "blouse", "color": "pink", "material": "silk", "gender": "female", "style": "formal", "brand": "Mango", "season": "spring", "price": 55, "description": "Pink silk blouse.", "usage_context": "Spring formal events."},
    {"id": 26, "item_type": "tie", "color": "blue", "material": "silk", "gender": "male", "style": "formal", "brand": "Hugo Boss", "season": "all", "price": 35, "description": "Blue silk tie.", "usage_context": "Business and formal occasions."},
    {"id": 27, "item_type": "socks", "color": "grey", "material": "cotton", "gender": "unisex", "style": "casual", "brand": "Uniqlo", "season": "all", "price": 8, "description": "Grey cotton socks.", "usage_context": "Everyday wear."},
    {"id": 28, "item_type": "gloves", "color": "black", "material": "leather", "gender": "female", "style": "formal", "brand": "Coach", "season": "winter", "price": 60, "description": "Black leather gloves.", "usage_context": "Winter formal events."},
    {"id": 29, "item_type": "vest", "color": "navy", "material": "wool", "gender": "male", "style": "formal", "brand": "Brooks Brothers", "season": "fall", "price": 70, "description": "Navy wool vest.", "usage_context": "Business and formal layering."},
    {"id": 30, "item_type": "hoodie", "color": "green", "material": "cotton", "gender": "unisex", "style": "sporty", "brand": "Nike", "season": "spring", "price": 45, "description": "Green cotton hoodie.", "usage_context": "Sport and casual wear."},
    {"id": 31, "item_type": "pajamas", "color": "blue", "material": "cotton", "gender": "female", "style": "casual", "brand": "Victoria's Secret", "season": "all", "price": 38, "description": "Blue cotton pajamas.", "usage_context": "Sleepwear."},
    {"id": 32, "item_type": "swimwear", "color": "red", "material": "nylon", "gender": "female", "style": "sporty", "brand": "Speedo", "season": "summer", "price": 48, "description": "Red nylon swimsuit.", "usage_context": "Swimming and beach."},
    {"id": 33, "item_type": "coat", "color": "black", "material": "wool", "gender": "male", "style": "formal", "brand": "Burberry", "season": "winter", "price": 300, "description": "Black wool coat.", "usage_context": "Winter business and formal."},
    {"id": 34, "item_type": "scarf", "color": "blue", "material": "cashmere", "gender": "female", "style": "formal", "brand": "Gucci", "season": "winter", "price": 120, "description": "Blue cashmere scarf.", "usage_context": "Winter luxury accessory."},
    {"id": 35, "item_type": "t-shirt", "color": "white", "material": "cotton", "gender": "male", "style": "casual", "brand": "Hanes", "season": "summer", "price": 10, "description": "Classic white t-shirt.", "usage_context": "Everyday summer wear."},
    {"id": 36, "item_type": "jeans", "color": "black", "material": "denim", "gender": "female", "style": "casual", "brand": "Levi's", "season": "all", "price": 55, "description": "Black denim jeans.", "usage_context": "Casual and night out."},
    {"id": 37, "item_type": "boots", "color": "black", "material": "leather", "gender": "male", "style": "casual", "brand": "Dr. Martens", "season": "fall", "price": 130, "description": "Black leather boots.", "usage_context": "Fall and winter casual."},
    {"id": 38, "item_type": "vest", "color": "grey", "material": "wool", "gender": "female", "style": "formal", "brand": "Zara", "season": "fall", "price": 65, "description": "Grey wool vest.", "usage_context": "Layering for business."},
    {"id": 39, "item_type": "hoodie", "color": "black", "material": "cotton", "gender": "male", "style": "sporty", "brand": "Adidas", "season": "fall", "price": 50, "description": "Black cotton hoodie.", "usage_context": "Sport and streetwear."},
    {"id": 40, "item_type": "socks", "color": "white", "material": "cotton", "gender": "unisex", "style": "casual", "brand": "Nike", "season": "all", "price": 9, "description": "White cotton socks.", "usage_context": "Everyday wear."},
]

outfits = [
    [1, 2, 9, 12],    # red shirt + blue jeans + white sneakers + brown belt
    [3, 11, 9],       # black silk dress + silver bracelet + white sneakers
    [4, 5, 9],        # white skirt + green jacket + white sneakers
    [6, 7, 10, 12],   # blue linen shirt + black cotton pants + black shoes + brown belt
    [8, 5, 9],        # red cotton dress + green jacket + white sneakers
    [1, 7, 10, 12],   # red shirt + black pants + black shoes + brown belt
    [6, 2, 10, 12],   # blue linen shirt + blue jeans + black shoes + brown belt
    [3, 11, 10],      # black silk dress + silver bracelet + black shoes
    [13, 7, 18],      # grey wool coat + black pants + brown boots
    [15, 2, 10, 12],  # navy blazer + blue jeans + black shoes + brown belt
    [16, 17, 24],     # beige shorts + yellow t-shirt + tan sandals
    [19, 21, 18, 20], # purple sweater + cream cardigan + brown boots + black hat
    [22, 23, 24],     # black leggings + white tank top + tan sandals
    [14, 1, 2, 9],    # red scarf + red shirt + blue jeans + white sneakers
    [5, 16, 9],       # green jacket + beige shorts + white sneakers
    [25, 4, 34, 18],  # pink blouse + white skirt + blue scarf + brown boots
    [26, 6, 29, 10],  # blue tie + blue linen shirt + navy vest + black shoes
    [27, 35, 2, 40],  # grey socks + white t-shirt + blue jeans + white socks
    [28, 13, 7, 18],  # black gloves + grey coat + black pants + brown boots
    [30, 16, 9, 40],  # green hoodie + beige shorts + white sneakers + white socks
    [31, 27, 40],     # blue pajamas + grey socks + white socks
    [32, 24, 14],     # red swimwear + tan sandals + red scarf
    [33, 29, 10, 26], # black coat + navy vest + black shoes + blue tie
    [36, 17, 24],     # black jeans + yellow t-shirt + tan sandals
    [37, 35, 40],     # black boots + white t-shirt + white socks
    [38, 25, 7, 11],  # grey vest + pink blouse + black pants + silver bracelet
    [39, 2, 40],      # black hoodie + blue jeans + white socks
    [40, 35, 2],      # white socks + white t-shirt + blue jeans
] 