try:
    from mpi4py import MPI
except ImportError:
    pass

info = {"likelihood": {'planck_2018_lowl.TT': None},
'params': {'As': {'latex': 'A_\\mathrm{s}',
                   'value': 'lambda logA: 1e-10*np.exp(logA)'},
            'DHBBN': {'derived': 'lambda DH: 10**5*DH',
                      'latex': '10^5 \\mathrm{D}/\\mathrm{H}'},
            'H0': {'latex': 'H_0',
                   'prior': {'max': 90, 'min': 30},
                   'proposal': 60,
                   'ref': {'dist': 'norm', 'loc': 67, 'scale': 2}},
            'YHe': {'latex': 'Y_\\mathrm{P}'},
            'Y_p': {'latex': 'Y_P^\\mathrm{BBN}'},
            'logA': {'drop': True,
                     'latex': '\\log(10^{10} A_\\mathrm{s})',
                     'prior': {'max': 3.91, 'min': 1.61},
                     'proposal': 2,
                     'ref': {'dist': 'norm', 'loc': 3.05, 'scale': 0.001}},
            'mnu': 0.06,
            'ns': {'latex': 'n_\\mathrm{s}',
                   'prior': {'max': 1.2, 'min': 0.8},
                   'proposal': 0.9,
                   'ref': {'dist': 'norm', 'loc': 0.965, 'scale': 0.004}},
            'ombh2': {'latex': '\\Omega_\\mathrm{b} h^2',
                      'prior': {'max': 0.1, 'min': 0.0001},
                      'proposal': 0.01,
                      'ref': {'dist': 'norm', 'loc': 0.0224, 'scale': 0.0001}},
            'omch2': {'latex': '\\Omega_\\mathrm{c} h^2',
                      'prior': {'max': 0.99, 'min': 0.001},
                      'proposal': 0.05,
                      'ref': {'dist': 'norm', 'loc': 0.12, 'scale': 0.001}},
            'omega_de': {'latex': '\\Omega_\\Lambda'},
            'omegam': {'latex': '\\Omega_\\mathrm{m}'},
            'omegamh2': {'derived': 'lambda omegam, H0: omegam*(H0/100)**2',
                         'latex': '\\Omega_\\mathrm{m} h^2'},
            'omk': {'latex': '\\Omega_k',
                    'prior': {'max': 0.3, 'min': -0.3},
                    'proposal': 0.001,
                    'ref': {'dist': 'norm', 'loc': -0.009, 'scale': 0.001}},
            'tau': {'latex': '\\tau_\\mathrm{reio}',
                    'prior': {'max': 0.8, 'min': 0.01},
                    'proposal': 0.03,
                    'ref': {'dist': 'norm', 'loc': 0.055, 'scale': 0.006}},
            'zrei': {'latex': 'z_\\mathrm{re}'}}}
info['sampler'] = {"polychord": {'nlive': 150, 'precision_criterion': 0.001}}
info['theory'] = {'camb': None}


from cobaya.run import run

updated_info, sampler = run(info)

# Export the results to GetDist
gd_sample = sampler.products(to_getdist=True)["sample"]

# Analyze and plot
mean = gd_sample.getMeans()[:]
print("Mean:")
print(mean)

from getdist.types import ResultTable
print(ResultTable(ncol=1,results=[gd_sample],
                 paramList=['As','DHBBN','H0','YHe','Y_p','logA','mnu','ombh2','omch2','omega_de','omegam','omegamh2','omk','tau','zrei'], limit=1, titles=['Planck CMB']).tableTex())

f = open("samples.txt", "w")

paramList=['As','DHBBN','H0','YHe','Y_p','logA','mnu','ombh2','omch2','omega_de','omegam','omegamh2','omk','tau','zrei']

for i in paramList:
    f.write(i + '\t')
f.write('\n')
for i in gd_sample:
    for j in range(len(i)):
        f.write(i[j])
        if j==(len(i)-1):
            f.write('\n')
        else:
            f.write('\t')
f.close()
