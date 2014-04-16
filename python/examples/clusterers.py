# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# clusterers.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import os
import weka.core.jvm as jvm
import examples.helper as helper
from weka.core.converters import Loader
from weka.clusterers import Clusterer
from weka.filters import Filter


def main():
    """
    Just runs some example code.
    """

    # load a dataset
    iris = helper.get_data_dir() + os.sep + "iris.arff"
    helper.print_info("Loading dataset: " + iris)
    loader = Loader("weka.core.converters.ArffLoader")
    data = loader.load_file(iris)

    # remove class attribute
    helper.print_info("Removing class attribute")
    remove = Filter("weka.filters.unsupervised.attribute.Remove")
    remove.set_options(["-R", "last"])
    remove.set_inputformat(data)
    data = remove.filter(data)

    # build a clusterer and output model
    helper.print_title("Training SimpleKMeans clusterer")
    clusterer = Clusterer(classname="weka.clusterers.SimpleKMeans")
    clusterer.set_options(["-N", "3"])
    clusterer.build_clusterer(data)
    print(clusterer)


if __name__ == "__main__":
    try:
        jvm.start()
        main()
    except Exception, e:
        print(e)
    finally:
        jvm.stop()