import mapnik
m = mapnik.Map(1024,600)
mapnik.load_map(m, "mapnik_world.xml")
m.zoom_all()
mapnik.render_to_file(m, "images/simple_map_2.png")
