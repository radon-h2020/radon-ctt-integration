# RADON Integration

[![Build Status](https://travis-ci.com/UST-CTT/radon-ctt-integration.svg?branch=master)](https://travis-ci.com/UST-CTT/radon-ctt-integration)

This setup integrates the following tools:
* arbitrary service templates from [RADON Particles](https://github.com/radon-h2020/radon-particles) (currently SockShop)
* [RADON GMT](https://github.com/radon-h2020/radon-gmt)
* [Opera](https://github.com/radon-h2020/xopera-opera)

## Major Integration Steps 
* Clone [RADON Particles](https://github.com/radon-h2020/radon-particles)
* Spin up [RADON GMT](https://github.com/radon-h2020/radon-gmt)
* Export specified CSAR using REST interface of RADON GMT
* Extract CSAR and identify entry definition
* Deploy said service templat with [Opera](https://github.com/radon-h2020/xopera-opera)
* Try to probe deployed service using `curl`

