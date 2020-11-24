# Copyright (C) 2013-2020 Echelon Corporation.  All Rights Reserved.
# Use of this code is subject to your compliance with the terms of the
# Echelon IzoT(tm) Software Developer's Kit License Agreement which is
# available at www.echelon.com/license/izot_sdk/.

# IzoT resources contained in this file are generated by an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.
# Names of resources and fields or members defined within a resource are
# derived from the same sources.  Names, capitalization and aspects of source
# code formatting may fail to comply with PEP-8 and PEP-257 recommendations
# due to the automated generation of these IzoT definitions.
# Generated at 18-Nov-2020 16:22.

"""temp_p standard datapoint type, originally defined in resource file set
standard 00:00:00:00:00:00:00:00-0.  """


import izot.resources.base
from izot.resources.standard import standard


class temp_p(izot.resources.base.Scaled):
    """temp_p standard datapoint type.  Temperature (degrees Celsius.)."""

    def __init__(self):
        super().__init__(
            size=2,
            signed=True,
            scaling=(0.01, 0),
            invalid=327.67,
            minimum=-273.17,
            maximum=327.67,
            scope=0,
            key=105
        )
        self._original_name = 'SNVT_temp_p'
        self._standard_datapoint_type = True
        self._definition = standard.add(self)



if __name__ == '__main__':
    # unit test code.
    item = temp_p()
    pass