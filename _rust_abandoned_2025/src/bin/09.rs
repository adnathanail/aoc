use std::cmp::max;
use image::{ImageBuffer, Rgb, RgbImage};
use imageproc::drawing::{draw_filled_circle_mut, draw_hollow_circle_mut, draw_line_segment_mut};
use imageproc::point::Point;

advent_of_code::solution!(9);

fn get_red_tile_coords(input: &str) -> Vec<[i32; 2]> {
    let mut out: Vec<[i32; 2]> = Vec::new();
    for line in input.lines() {
        let coord: Vec<i32> = line.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        out.push([coord[0], coord[1]]);
    }
    out
}

fn get_square_size(c1: [i32; 2], c2: [i32; 2]) -> i32 {
    ((c1[0] - c2[0]).abs() + 1) * ((c1[1] - c2[1]).abs() + 1)
}

// fn render_polygon(coords: &Vec<[i32; 2]>, width: u32, height: u32, filename: &str) -> Result<(), image::ImageError> {
//     if coords.is_empty() {
//         return Ok(());
//     }

//     // Create a white background image
//     let mut img: RgbImage = ImageBuffer::from_pixel(width, height, Rgb([255u8, 255u8, 255u8]));

//     // Find bounding box of coordinates
//     let min_x = coords.iter().map(|c| c[0]).min().unwrap();
//     let max_x = coords.iter().map(|c| c[0]).max().unwrap();
//     let min_y = coords.iter().map(|c| c[1]).min().unwrap();
//     let max_y = coords.iter().map(|c| c[1]).max().unwrap();

//     let data_width = max_x - min_x;
//     let data_height = max_y - min_y;

//     println!("Coordinate bounds: x=[{}, {}], y=[{}, {}]", min_x, max_x, min_y, max_y);
//     println!("Data dimensions: {}x{}", data_width, data_height);

//     // Calculate scale to fit data in image with some padding
//     let padding = 10.0;
//     let scale_x = (width as f32 - 2.0 * padding) / data_width as f32;
//     let scale_y = (height as f32 - 2.0 * padding) / data_height as f32;
//     let scale = scale_x.min(scale_y);

//     println!("Using scale: {}", scale);

//     // Convert and scale coordinates to Point<i32>
//     let points: Vec<Point<i32>> = coords
//         .iter()
//         .map(|coord| {
//             let x = ((coord[0] - min_x) as f32 * scale + padding) as i32;
//             let y = ((coord[1] - min_y) as f32 * scale + padding) as i32;
//             Point::new(x, y)
//         })
//         .collect();

//     // Draw lines connecting consecutive points
//     let red = Rgb([255u8, 0u8, 0u8]);
//     for i in 0..points.len() {
//         let p1 = points[i];
//         let p2 = points[(i + 1) % points.len()];
//         draw_line_segment_mut(&mut img, (p1.x as f32, p1.y as f32), (p2.x as f32, p2.y as f32), red);
//     }

//     // Draw circles at each point
//     let blue = Rgb([0u8, 0u8, 255u8]);
//     for point in &points {
//         draw_filled_circle_mut(&mut img, (point.x, point.y), 3, blue);
//     }

//     // Save the image
//     img.save(filename)
// }

pub fn part_one(input: &str) -> Option<i32> {
    let red_tile_coords = get_red_tile_coords(input);
    let mut largest_square_size = 0;
    for i in 0..(red_tile_coords.len() - 1) {
        for j in (i + 1)..red_tile_coords.len() {
            largest_square_size = max(largest_square_size, get_square_size(red_tile_coords[i], red_tile_coords[j]))
        }
    }
    Some(largest_square_size)
}

pub fn part_two(input: &str) -> Option<u64> {
    let red_tile_coords = get_red_tile_coords(input);
    // let _ = render_polygon(&red_tile_coords, 800, 800, "output.png");
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(50));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(24));
    }
}
