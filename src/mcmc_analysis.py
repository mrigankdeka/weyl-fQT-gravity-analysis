'''Our goal now is to calculate how well the model matches the data. In the paper, The deceleration parameter is defined as:
q(z) = q0 + q1*z(1+z)/(1+z^2)
where q0 and q1 are free parameters (as their values aren't predetermined and are obtained from the fitting/optimizing process)
Here, q0 = q(z=0) is the current value of the deceleration parameter (i.e. today) and q1 controls how strongly the deceleration parameter changes with redshift z. Hence we are interested in the parameter space (q0,q1)'''

import numpy as np
def log_likelihood_OHD(params, z_data, H_data, H_err):
    
    q0, q1 = params
    
    # Now we shall calculate what our model predicts at each redshift
    H_model = 70 * (1 + z_data)**(1 + q0) * (1 + z_data**2)**(q1 / 2)
    
    # Let's now calculate the difference between model and data
    residuals = H_data - H_model
    
    # To find the measure of misfit, we will calculate chi-squared (measure of misfit) as we assume likelihood function follows a normal distribution
    chi2 = np.sum((residuals / H_err)**2)
    
    # For MCMC, we use the standard formula for log-likelihood
    log_like = -0.5 * chi2
    
    return log_like


'''Now we shall add the prior function which tells us the probability of finding a certain value of the parameters (q0,q1) before observing the data we have now
 i.e. what we believe about the parameters (q0,q1) before conducting the experiment. As the universe is accelerating in the current epoch, the deceleration parameter value today i.e. q0 <0 and q1>0 (deceleration to acceleration transition)'''

def log_prior_OHD(params):
    q0,q1 = params

    if -0.8 < q0 < -0.4 and 0.5 < q1 < 0.8:
        return 0.0               #all parameters are reasonable and within expected range
    else: 
        return -np.inf           #these parameter values can never be obtained




'''Now we shall try to evaluate the log of the posterior function i.e. the log of the probability of finding the parameter value given we observed the data.
As we know, Posterior ∝ Likelihood × Prior ⇒ log_posterior = log_likelihood + log_prior
we need to maximize log_posterior'''

def log_posterior_OHD(params, z_data, H_data, H_err):
    q0,q1 = params

    if np.isfinite(log_prior_OHD(params)):
        return log_prior_OHD(params) + log_likelihood_OHD(params, z_data, H_data, H_err)
    else:
        return -np.inf

def chi2_OHD(params, z_data, H_data, H_err, H0=70):
    q0, q1 = params

    H_model = H0 * (1 + z_data)**(1 + q0) * (1 + z_data**2)**(q1 / 2)

    residuals = H_data - H_model

    return np.sum((residuals / H_err)**2)



from cosmology import distance_modulus_theory, hubble_z


def chi2_SNeIa(params, zcmb, mb, dmb, H0=70):
    q0, q1, M_B = params

    mu_th = distance_modulus_theory(zcmb, q0, q1, H0)

    residuals = mb - M_B - mu_th

    return np.sum((residuals / dmb)**2)


def log_likelihood_SNeIa(params, zcmb, mb, dmb):
    return -0.5 * chi2_SNeIa(params, zcmb, mb, dmb)


def log_prior_SNeIa(params):
    q0, q1, M_B = params

    if -0.8 < q0 < -0.4 and 0.5 < q1 < 0.8 and -20 < M_B < -18:
        return 0.0

    return -np.inf


def log_posterior_SNeIa(params, zcmb, mb, dmb):
    q0, q1, M_B = params

    if np.isfinite(log_prior_SNeIa(params)):
        return log_prior_SNeIa(params) + log_likelihood_SNeIa(params, zcmb, mb, dmb)

    else:
        return -np.inf




def log_likelihood_combined(params, z_ohd, H_ohd, H_err, zcmb, mb, dmb, H0=69):

    q0, q1, M_B = params

    chi2_hub = chi2_OHD((q0, q1), z_ohd, H_ohd, H_err, H0)
    chi2_sn  = chi2_SNeIa(params, zcmb, mb, dmb, H0)

    return -0.5 * (chi2_hub + chi2_sn)


def log_posterior_combined(params, z_ohd, H_ohd, H_err, zcmb, mb, dmb, H0=70):
    q0, q1, M_B = params

    if np.isfinite(log_prior_SNeIa(params)):
        return log_prior_SNeIa(params) + log_likelihood_combined(params, z_ohd, H_ohd, H_err, zcmb, mb, dmb, H0 = 70)

    else:
        return -np.inf  
    