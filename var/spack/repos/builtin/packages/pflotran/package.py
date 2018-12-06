# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Pflotran(AutotoolsPackage):
    """PFLOTRAN is an open source, state-of-the-art massively parallel
       subsurface flow and reactive transport code.
    """

    homepage = "http://www.pflotran.org"
    git      = "https://bitbucket.org/pflotran/pflotran.git"

    version('develop')
    version('xsdk-0.4.0', commit='6c8baef2166ceb49cc3e09458fd64bbefc3cebe2')
    version('xsdk-0.3.0', branch='release/xsdk-0.3.0')
    version('xsdk-0.2.0', commit='4da763c6136df57caff43f98c926433958cfdea6')

    depends_on('mpi')
    depends_on('hdf5@1.8.12:+mpi+fortran')
    depends_on('petsc@develop:+hdf5+metis', when='@develop')
    depends_on('petsc@3.10:+hdf5+metis', when='@xsdk-0.4.0')
    depends_on('petsc@xsdk-0.2.0+hdf5+metis', when='@xsdk-0.2.0')
    depends_on('petsc@3.8.0:+hdf5+metis', when='@xsdk-0.3.0')

    @property
    def parallel(self):
        return (self.spec.satisfies('@develop') or
                self.spec.satisfies('@xsdk-0.4.0'))
