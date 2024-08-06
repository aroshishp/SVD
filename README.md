### Singular Value Decomposition

This repository contains the codes and outputs of implementing Singular Value Decomposition from scratch and using the algorithm to compress images.
The images were first compressed in grayscale mode and the same method was extended to RGB matrices.

The repository contains the following:
1. **Code**: The [SVD_imageCompression.ipynb](https://github.com/aroshishp/SVD/blob/main/SVD_imageCompression.ipynb) notebook contains the following:
   * Theory of SVD and Applications
   * Implementation of SVD from scratch and verifying by remultiplying
   * Comparison with the in-built SVD function provided by NumPy's Linear Algebra library
   * Image Compression and Quality Enhancement in grayscale. The SVD function is stored in [svd_module.py](https://github.com/aroshishp/SVD/blob/main/svd_module.py).
   * Extension of above to RGB
   * The images used are [quality.jpeg](https://github.com/aroshishp/SVD/blob/main/quality.jpeg), [quality1.jpeg](https://github.com/aroshishp/SVD/blob/main/quality1.jpeg) and [img3.jpg](https://github.com/aroshishp/SVD/blob/main/img3.jpg). The output images are stored in Images (grayscale) and Images_RGB (colored).
   * Report on findings
2. **Report**: The [Epoch_Session_1_Report.pdf](https://github.com/aroshishp/SVD/blob/main/Epoch_Session_1_Report.pdf) is the overall report for this hackathon.
   The [Epoch_Session_1_LR.pdf](https://github.com/aroshishp/SVD/blob/main/Epoch_Session_1_LR.pdf) is my learning report before and after session 1.
3. **Interactive Tool**: The alorithm was used to create an interface where a user could upload an image and observe the impact of k values in real-time. The code for it is provided in [interactiveTool.py](https://github.com/aroshishp/SVD/blob/main/interactiveTool.py). Run the following commands to run it locally:
   
   i. Install Streamlit, if not installed, using:
      ```
       pip install streamlit
      ```
   ii. Run the following command:
     ```
     streamlit run interactiveTool.py
     ```
     The tool will open on a browser. The image can be uploaded in jpg, jpeg or png formats. The code will run automatically and display the compressed image along with a slider to adjust k values. A download button is also provided to download the required image. A demo is provided below.
