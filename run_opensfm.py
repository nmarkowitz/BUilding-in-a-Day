import argparse
import subprocess
import os

def run_docker(dataset_path, container_name):

    dataset_name = os.path.basename(dataset_path)
    # Define the Docker command
    run_all_command = [
        'docker', 'run', '--rm',                                        # Tell docker to run
        '-v', f'{dataset_path}:/source/OpenSfM/data/{dataset_name}',    # Mount host directory
        container_name,                                                 # Name of the container to run in
        '/source/OpenSfM/bin/opensfm_run_all',                          # Command to run
        f'/source/OpenSfM/data/{dataset_name}',                         # Where in docker is the files of interest
    ]

    compute_statistics_command = [
        'docker', 'run', '--rm',                                        # Tell docker to run
        '-v', f'{dataset_path}:/source/OpenSfM/data/{dataset_name}',    # Mount host directory
        container_name,                                                 # Name of the container to run in
        '/source/OpenSfM/bin/opensfm compute_statistics',               # Command to run
        f'/source/OpenSfM/data/{dataset_name}',                         # Where in docker is the files of interest
    ]

    export_report_command = [
        'docker', 'run', '--rm',                                        # Tell docker to run
        '-v', f'{dataset_path}:/source/OpenSfM/data/{dataset_name}',    # Mount host directory
        container_name,                                                 # Name of the container to run in
        '/source/OpenSfM/bin/opensfm export_report',                    # Command to run
        f'/source/OpenSfM/data/{dataset_name}',                         # Where in docker is the files of interest
    ]



    # Run the Docker command
    try:
        print("Starting Docker container...")
        subprocess.run(run_all_command, check=True)
        subprocess.run(compute_statistics_command, check=True)
        subprocess.run(export_report_command, check=True)
        print("Docker container has completed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Docker: {e}")

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='Run OpenSfM in a Docker container.')
    parser.add_argument('-d', '--dataset', required=True, help='Path to the dataset directory')
    parser.add_argument('-c', '--container', required=True, help='Name of the Docker container to run')

    args = parser.parse_args()

    # Run the Docker function
    run_docker(args.dataset, args.container)

if __name__ == "__main__":
    main()
