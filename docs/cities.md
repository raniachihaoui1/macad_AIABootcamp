# City Assignments

Each student picks (or is assigned) one city from the table below, then **chooses a district / neighbourhood** within it. Fetching a whole city returns too much data and overloads the API — always scope to a district.

> **Format:** `"District, City, Country"` — e.g. `"Södermalm, Stockholm, Sweden"`. Verify on [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org/) that the name resolves.

| # | City | Example district | Region | Est. amenities | Notes |
|---|------|-----------------|--------|----------------|-------|
| 1 | Stockholm | Södermalm, Östermalm, Kungsholmen | Europe | ~500–1 500 | Swedish + English tags |
| 2 | Göteborg | Centrum, Majorna, Hisingen | Europe | ~400–1 000 | Heavy `name:sv`, Lantmäteriet artifacts |
| 3 | Malmö | Centrum, Möllevången, Västra Hamnen | Europe | ~300–700 | Smaller, good for beginners |
| 4 | Berlin | Kreuzberg, Mitte, Prenzlauer Berg | Europe | ~800–2 000 | German + English + Turkish tags |
| 5 | Amsterdam | Centrum, De Pijp, Jordaan | Europe | ~500–1 200 | Dutch naming conventions |
| 6 | Barcelona | el Poblenou, Gràcia, el Born | Europe | ~600–1 500 | Catalan + Spanish + English |
| 7 | Paris | Le Marais, Montmartre, Belleville | Europe | ~800–2 000 | French opening_hours formats |
| 8 | Vienna | Innere Stadt, Leopoldstadt, Neubau | Europe | ~500–1 200 | Use `"Wien"` not `"Vienna"` |
| 9 | Prague | Staré Město, Vinohrady, Žižkov | Europe | ~400–1 000 | Use `"Praha"` not `"Prague"` |
| 10 | Rome | Trastevere, Monti, Testaccio | Europe | ~600–1 500 | Many `cuisine` tags |
| 11 | Lisbon | Alfama, Bairro Alto, Belém | Europe | ~300–800 | Portuguese tags |
| 12 | Helsinki | Kallio, Kruununhaka, Töölö | Europe | ~300–700 | Finnish + Swedish bilingual |
| 13 | Copenhagen | Indre By, Nørrebro, Vesterbro | Europe | ~400–1 000 | Use `"København"` |
| 14 | Dublin | Temple Bar, Portobello, Rathmines | Europe | ~300–700 | Many pubs tagged differently |
| 15 | Tokyo | 渋谷区, 新宿区, 中央区 | Asia | ~1 000–3 000 | Filter by ward. Japanese encoding |
| 16 | Seoul | 강남구, 종로구, 마포구 | Asia | ~800–2 500 | Korean + English |
| 17 | New York | Brooklyn, Manhattan, Queens | N. America | ~2 000–5 000 | Filter by borough |
| 18 | Portland | Pearl District, Hawthorne, Alberta | N. America | ~300–800 | Well-mapped, good OSM community |
| 19 | Buenos Aires | Palermo, San Telmo, Recoleta | S. America | ~500–1 200 | Spanish tags |
| 20 | Cape Town | City Bowl, Woodstock, Sea Point | Africa | ~200–600 | English + Afrikaans, sparser |

## Tips

- **Always pick a district** — not the whole city. This keeps requests under ~1 500 features and avoids API rate limiting.
- **Non-Latin names**: the place string must be geocodable by Nominatim — check on [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org/) first
- **Similar cities** are fine: two students can both do European capitals — the data issues will differ

## OSMnx Fetch Template

```python
import osmnx as ox

PLACE = "Your District, Your City, Country"

AMENITY_TYPES = [
    "restaurant", "cafe", "fast_food", "bar", "pub",
    "pharmacy", "hospital", "clinic", "dentist",
    "school", "university", "library", "kindergarten",
    "bank", "atm", "post_office",
]

gdf = ox.features_from_place(PLACE, tags={"amenity": AMENITY_TYPES})
```
