#include <opencv2/opencv.hpp>

int main() {
    cv::Mat image = cv::imread("111.webp", cv::IMREAD_COLOR);
    if(image.empty()) {
        std::cout << "Could not open or find the image" << std::endl;
        return -1;
    }
    cv::namedWindow("Test Image", cv::WINDOW_AUTOSIZE);
    cv::imshow("Test Image", image);
    cv::waitKey(0);
    return 0;
}