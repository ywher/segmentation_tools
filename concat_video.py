import cv2
import numpy as np
import argparse
import tqdm

class VideoConcatenator:
    def __init__(self, inputs, interval, output, resize, columns):
        self.inputs = inputs
        self.interval = interval
        self.output = output
        self.resize = resize
        self.columns = columns
        self.fps = None
        self.width = None
        self.height = None
        self.total_frames = None
        self.interval_frames = None
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    def get_video_info(self, cap):
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        return fps, width, height, total_frames
    
    def concatenate(self):
        # Open input video files
        caps = []
        for input_file in self.inputs:
            caps.append(cv2.VideoCapture(input_file))

        # Get video properties from the first input video
        self.fps, self.width, self.height, self.total_frames = self.get_video_info(caps[0])
        self.interval_frames = int(self.interval * self.fps)
        total_inputs = len(self.inputs)
        
        # Resize dimensions
        resized_width = int(self.resize[0])
        resized_height = int(self.resize[1])

        # Calculate rows and columns for displaying videos
        rows = (total_inputs + 1) // self.columns  # Ceiling division
        
        # Calculate output video dimensions
        out_width = self.columns * resized_width + (self.columns - 1) * self.interval
        out_height = rows * resized_height + (rows - 1) * self.interval

        # Create output video file
        out = cv2.VideoWriter(self.output, self.fourcc, self.fps, (out_width, out_height))

        # Iterate through frames
        bar = tqdm.tqdm(total=self.total_frames)
        for i in range(self.total_frames):
            frames_concat = []
            for j in range(total_inputs):
                ret, frame = caps[j].read()
                if ret:
                    frame_resized = cv2.resize(frame, (resized_width, resized_height))
                    frames_concat.append(frame_resized)
                else:
                    break
            
            if len(frames_concat) == total_inputs:
                frame_concat = np.zeros((out_height, out_width, 3), np.uint8)
                for k in range(total_inputs):
                    row_start = k // self.columns * (resized_height + self.interval)
                    row_end = row_start + resized_height
                    col_start = k % self.columns * (resized_width + self.interval)
                    col_end = col_start + resized_width
                    frame_concat[row_start:row_end, col_start:col_end] = frames_concat[k]
                    # frame_concat[k // self.columns * (resized_height + self.interval): k // self.columns * (resized_height + self.interval) + resized_height, k % self.columns * (resized_width + self.interval): k % self.columns * (resized_width + self.interval) + resized_width] = frames_concat[k]
                # frame_concat = frames_concat[0]
                # for k in range(1, total_inputs):
                #     frame_concat = np.concatenate((frame_concat, np.zeros((resized_height, self.interval, 3), np.uint8), frames_concat[k]), axis=1)
                out.write(frame_concat)
            else:
                break
            bar.update(1)
        bar.close()

        # Release resources and close the output video file
        for cap in caps:
            cap.release()
        out.release()

        print('Done!')

def main(args):
    vc = VideoConcatenator(args.inputs, args.interval, args.output, args.resize, args.columns)
    vc.concatenate()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video Concatenator')
    parser.add_argument('--inputs', type=str, nargs='+', required=True, help='input video paths')
    parser.add_argument('--interval', type=int, default=10, help='interval distance between two videos')
    parser.add_argument('--output', type=str, required=True, help='output video path')
    parser.add_argument('--resize', type=int, nargs=2, default=[512, 256], help='resize dimensions (width height)')
    parser.add_argument('--columns', type=int, default=2, help='number of columns for displaying videos')
    args = parser.parse_args()

    main(args)
