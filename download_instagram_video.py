import instaloader
# specify path to save video
def download_instagram_video(post_url, download_folder="Videos"): 
    """
    Download an Instagram video using Instaloader.

    :param post_url: URL of the Instagram post.
    :param download_folder: Folder to save the video.
    """
    # Create an instance of Instaloader
    loader = instaloader.Instaloader(download_video_thumbnails=False, save_metadata=False)
    
    # Extract the shortcode from the post URL
    try:
        shortcode = post_url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        if post.is_video:
            # Download the video
            loader.download_post(post, target=download_folder)
            print(f"Video downloaded to {download_folder}")
        else:
            print("The provided URL does not point to a video.")
    except Exception as e:
        print(f"Error downloading video: {e}")

# Example usage
if __name__ == "__main__":
    post_url = input("Enter the Instagram post URL: ")
    download_instagram_video(post_url)
