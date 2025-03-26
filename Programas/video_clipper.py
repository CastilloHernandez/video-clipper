import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip


def extract_clips(input_file, output_dir, duration, interval):
    try:
        # Carga el video original
        video = VideoFileClip(input_file)
        total_duration = video.duration

        if duration == 0:
            # Modo de extracción de imágenes
            start_time = 0
            frame_index = 1

            while start_time < total_duration:
                # Extrae un fotograma en el tiempo especificado
                frame = video.get_frame(start_time)
                output_path = f"{output_dir}/frame_{frame_index}.jpg"

                # Guarda el fotograma como archivo de imagen
                from PIL import Image
                image = Image.fromarray(frame)
                image.save(output_path)

                print(f"Frame {frame_index} guardado en: {output_path}")

                frame_index += 1
                start_time += interval

            print("Extracción de imágenes completada.")
        else:
            # Modo de extracción de clips
            start_time = 0
            clip_index = 1

            while start_time < total_duration:
                end_time = min(start_time + duration, total_duration)

                # Extrae el clip del video
                clip = video.subclip(start_time, end_time)
                output_path = f"{output_dir}/clip_{clip_index}.avi"

                # Escribe el clip en un archivo
                clip.write_videofile(output_path, codec="mpeg4")

                print(f"Clip {clip_index} guardado en: {output_path}")

                clip_index += 1
                start_time += interval

            print("Extracción de clips completada.")

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Extrae clips o imágenes de un video AVI.")

    parser.add_argument("input_file", type=str, help="Ruta al archivo de video de entrada (AVI).")
    parser.add_argument("output_dir", type=str, help="Directorio donde se guardarán los clips o imágenes extraídos.")
    parser.add_argument("--duration", type=int, required=True, help="Duración de cada clip en segundos (0 para extraer imágenes).")
    parser.add_argument("--interval", type=int, required=True, help="Intervalo entre clips o imágenes en segundos.")

    args = parser.parse_args()

    extract_clips(args.input_file, args.output_dir, args.duration, args.interval)


if __name__ == "__main__":
    main()
