# =============================================================================
# Student Configuration: Data Layout Booleans
# =============================================================================
#
# You are computing C = A * B where A ∈ R^{M×H}, B ∈ R^{H×N}, C ∈ R^{M×N}.
#
# The PE grid has kernel_x_dim columns and kernel_y_dim rows.
#
# Global layout controls how matrix blocks map to PEs:
#   False = "natural": matrix-rows along Y-PEs, matrix-cols along X-PEs
#   True  = "transposed": matrix-rows along X-PEs, matrix-cols along Y-PEs
#
# Memory layout controls how each local block is stored:
#   False = row-major in natural orientation
#   True  = store the transpose (row-major of the transposed block)
#
# Hint: think about which dimension needs to be contiguous in memory for
# efficient DSD access (broadcast columns of B, SAXPY with columns of A,
# write columns into C).
# =============================================================================

# --- Matrix A (M x H) ---
A_GLOBAL_TRANSPOSE = False  # M→Y, H→X => local block is (dM, dH) = (M/Ky, H/Kx)
A_MEMORY_TRANSPOSE = True   # store column-major so A columns (length dM) are contiguous for SAXPY

# --- Matrix B (H x N) ---
B_GLOBAL_TRANSPOSE = True   # H→X, N→Y => local block is (dH, dN_y) = (H/Kx, N/Ky)
B_MEMORY_TRANSPOSE = True   # store column-major so B columns (length dH) are contiguous for broadcast

# --- Matrix C (M x N) ---
C_GLOBAL_TRANSPOSE = False  # M→Y, N→X => local block is (dM, dN) = (M/Ky, N/Kx)
C_MEMORY_TRANSPOSE = True   # store column-major so C columns (length dM) are contiguous for reduction writes

