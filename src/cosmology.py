'''Here we are trying to calculate the Hubble parameter from the divergence-free deceleration parameter using the equation 22 from the paper: 
    H(z) = H0*(1+z)^(1+q0)*(1+z^2)^(q1/2). The Parameters space is (z,q0,q1) where:
    z= redshift (float or array)
    q0, q1= model parameters
    and H0 = 69 km/s/Mpc 
    It returns the Hubble function H= Hubble parameter at redshift z. We will perform a basic test to check if our model gives H0 at z = 0.'''

import numpy as np
import matplotlib.pyplot as plt

def hubble_z(z, q0, q1, H0=69):
    return H0*(1 + z)**(1 + q0) * (1 + z**2)**(q1 / 2)

# Test the function with some values
def test_hubble_function():
    z_values = np.array([0, 0.5, 1.0, 1.5, 2.0])
    
    # Test with some reasonable parameter values
    q0, q1 = -0.553, 0.698  # Roughly from the paper's table
    
    H_values = hubble_z(z_values, q0, q1)
    
    print("Testing Hubble function:")
    print("z\tH(z)")
    for z, H in zip(z_values, H_values):
        print(f"{z}\t{H:.2f}")
    
    return z_values, H_values

# Running the test
z_test, H_test = test_hubble_function()


'''In the paper, the authors have used a certain formulation of the distance modulus (equation 27) to calculate the luminosity distances of 1048 Type Ia supernovae:
   μ = m - M and to calculate the luminosity distance (equation 28) they have used dₗ(z) = c(1+z) ∫₀ᶻ dz'/H(z') '''

    


from scipy.integrate import quad

#Speed of light in km/s
c = 299792.458


def luminosity_distance(z, q0, q1, H0):


    def integrand(z_prime):
        return 1.0 / hubble_z(z_prime, q0, q1, H0=69)

    if np.isscalar(z):
        integral, _ = quad(integrand, 0, z)
        return c * (1 + z) * integral

    dL = np.zeros_like(z)
    for i, zi in enumerate(z):
        integral, _ = quad(integrand, 0, zi)
        dL[i] = c * (1 + zi) * integral

    return dL


def distance_modulus_theory(z, q0, q1, H0):
    
    dL = luminosity_distance(z, q0, q1, H0)
    return 5 * np.log10(dL) + 25


    