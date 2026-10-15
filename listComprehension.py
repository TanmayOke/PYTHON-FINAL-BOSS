sq=[x**2 for x in range(1,15)]
print(sq)

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy story"
, "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Wi 11 Hunting",
           "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day",
"Close Encounters of the Third Kind"]

new_list=[str for str in movies if str.startswith("G")]
print(new_list)