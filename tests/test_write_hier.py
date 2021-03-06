"""Tests alternate OBOReader."""

import os
import sys
import timeit
import datetime

from goatools.obo_parser import GODag

#################################################################
# Sub-routines to tests
#################################################################
def write_hier_all(dag, out):
    """write_hier.py: Prints the entire mini GO hierarchy, with counts of children."""
    out.write('\nTEST ALL: Print all hierarchies:\n')
    dag.write_hier("GO:0000001", out, num_child=True)


def write_hier_norep(dag, out):
    """Shortens hierarchy report by only printing branches once.

         Prints the 'entire hierarchy' of GO:0000005 the 1st time seen:

           ---     1 GO:0000005    L-02    D-02
           ----     0 GO:0000010   L-03    D-04

         Prints just GO:0000005 (ommit child GO:10) the 2nd time seen:

           ===     1 GO:0000005    L-02    D-02

         '=' is used in hierarchy mark to indicate that the pathes
             below the marked term have already been printed.
    """
    out.write('\nTEST ALL: Print branches just once:\n')
    dag.write_hier("GO:0000001", out, num_child=True, short_prt=True)


def write_hier_lim(dag, out):
    """Limits hierarchy list to GO Terms specified by user."""
    go_omit = ['GO:0000005', 'GO:0000010']
    go_ids = [go_id for go_id in dag if go_id not in go_omit]
    out.write('\nTEST OMIT: 05->10:\n')
    dag.write_hier("GO:0000001", out, include_only=go_ids)
      #go_marks=[oGO.id for oGO in oGOs_in_cluster])

def write_hier_mrk(dag, out):
    """Print all paths, but mark GO Terms of interest. """
    mark_lst = ['GO:0000001', 'GO:0000003', 'GO:0000006', 'GO:0000008', 'GO:0000009']
    out.write('\nTEST MARK: 01->03->06->08->09:\n')
    dag.write_hier("GO:0000001", out, go_marks=mark_lst)
      #go_marks=[oGO.id for oGO in oGOs_in_cluster])

#################################################################
# Tests
#################################################################
def test_all():
    """Run numerous tests for various reports."""
    dag_fin = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/mini_obo.obo")
    tic = timeit.default_timer()
    dag = GODag(dag_fin)
    toc = timeit.default_timer()
    out = sys.stdout
    write_hier_all(dag, out)
    write_hier_norep(dag, out)
    write_hier_lim(dag, out)
    write_hier_mrk(dag, out)
    msg = "Elapsed HMS: {}\n\n".format(str(datetime.timedelta(seconds=(toc-tic))))
    sys.stdout.write(msg)

#################################################################
# main
#################################################################
if __name__ == '__main__':
    test_all()
