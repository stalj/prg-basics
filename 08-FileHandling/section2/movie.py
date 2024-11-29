movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

file_name = 'movie_details.txt'

with open(file_name, 'w') as file:
   file.write(f"Movie Title: {movie_title}\n")
   file.write(f"Director: {director}\n")
   file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")