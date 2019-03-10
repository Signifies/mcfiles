import math, Image

start_time = 12 * 60
minute_step = 1
total_steps = 24 * 60
cell_size = 32
cell_count = total_steps / minute_step

x_offset = 7  # int(math.floor((cell_size - 17) / 2))
y_offset = 13 # int(math.floor((cell_size - 5) / 2))

width = cell_size
height = cell_size * cell_count

base = Image.open("clock-base.png")
top = Image.open("clock-top.png")
image = Image.new("RGBA", (width, height))

digit_maps = [
	"111101101101111",
	"001001001001001",
	"111001111100111",
	"111001011001111",
	"101101111001001",
	"111100111001111",
	"100100111101111",
	"111001001001001",
	"111101111101111",
	"111101111001001"
]

time = start_time
for y in range(0, cell_count):
	hour = math.floor(time / 60)
	hour = str(int(hour)).zfill(2)
	minute = (time % 60)
	minute = str(int(minute)).zfill(2)
	digits = hour + minute

	image.paste(base, (0, y * cell_size), base)

	for digit_index in range(4):
		digit = digits[digit_index]
		for dy in range(5):
			for dx in range(3):
				if digit_maps[int(digit)][dy * 3 + dx] == "1":
					image.putpixel((x_offset + dx + digit_index * 4 + (2 if (digit_index >= 2) else 0), y_offset + y * cell_size + dy), 0xff181616)
	image.putpixel((x_offset + (2 * 4), y_offset + y * cell_size + 4), 0xff181616)
	image.putpixel((x_offset + (2 * 4), y_offset + y * cell_size + 2), 0xff181616)

	image.paste(top, (0, y * cell_size), top)

	time += minute_step
	time %= total_steps

image.save("clock.png")
