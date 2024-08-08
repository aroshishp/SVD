import streamlit as st
import numpy as np
from PIL import Image
from svd_module import SVD
import io

def compress_image(A, k):
    R, G, B = A[:,:,0], A[:,:,1], A[:,:,2]

    # U_R, Sigma_R, VT_R = SVD(R)
    # U_G, Sigma_G, VT_G = SVD(G)
    # U_B, Sigma_B, VT_B = SVD(B)
    U_R, Sigma_R, VT_R = np.linalg.svd(R, full_matrices=False)
    U_G, Sigma_G, VT_G = np.linalg.svd(G, full_matrices=False)
    U_B, Sigma_B, VT_B = np.linalg.svd(B, full_matrices=False)

    R_k = U_R[:, :k] @ np.diag(Sigma_R[:k]) @ VT_R[:k, :]
    G_k = U_G[:, :k] @ np.diag(Sigma_G[:k]) @ VT_G[:k, :]
    B_k = U_B[:, :k] @ np.diag(Sigma_B[:k]) @ VT_B[:k, :]

    R_k = np.clip(R_k, 0, 255).astype(np.uint8)
    G_k = np.clip(G_k, 0, 255).astype(np.uint8)
    B_k = np.clip(B_k, 0, 255).astype(np.uint8)

    A_k = np.stack((R_k, G_k, B_k), axis=2)
    return A_k

def main():
    st.title("Image Compression using SVD")
    st.write("Upload an image and choose the level of compression (higher k, lower compression).")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        A = np.array(image, dtype=float)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

        k = st.slider("Select number of singular values (k)", min_value=1, max_value=min(A.shape[0], A.shape[1]), value=50)

        compressed_image = compress_image(A, k)

        with col2:  
            st.subheader(f"Compressed Image (k={k})")
            st.image(compressed_image, use_column_width=True)

        compressed_image_pil = Image.fromarray(compressed_image)
        buf = io.BytesIO()
        compressed_image_pil.save(buf, format="JPEG", quality=25)
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Compressed Image",
            data=byte_im,
            file_name=f"compressed_image_k_{k}.jpg",
            mime="image/jpeg"
        )

if __name__ == "__main__":
    main()