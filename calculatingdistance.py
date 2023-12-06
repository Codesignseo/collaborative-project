def render_time(vertex_count, renderer):
    if renderer == 'Eevee':
        m = (0.22 - 0.35) / (4608 - 24322)
        b = 0.35 - m * 24322
    elif renderer == 'Cycles':
        m = (7.71 - 38.18) / (4608 - 24322)
        b = 38.18 - m * 24322
    else:
        print("Invalid renderer. Please choose 'Eevee' or 'Cycles'.")
        return

    # Calculate render time using the linear equation
    time = m * vertex_count + b

    print(f"Expected render time for {renderer} with {vertex_count} vertices: {time:.2f} seconds")

# Get user input
renderer_input = input("Enter the renderer (Eevee or Cycles): ")
vertex_count_input = int(input("Enter the number of vertices: "))

# Call the function
render_time(vertex_count_input, renderer_input)
