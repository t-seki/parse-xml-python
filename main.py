import lxml.etree
import sys
from memory_profiler import profile
from measurement import Measurement


@profile
def use_parse():
    measurement = Measurement()

    obj = lxml.etree.parse('SwissProt.xml')
    root = obj.getroot()
    for entry in root.iter('Entry'):
        measurement.increment_count()

    print(f'elapsed_time(use_parse): {measurement.elapsed_time}')
    print(f'count: {measurement.count}')


@profile
def use_iter():
    measurement = Measurement()

    context = lxml.etree.iterparse('SwissProt.xml', events=('end',), tag='Entry')

    for event, elem in context:
        measurement.increment_count()

    print(f'elapsed_time(use_iter): {measurement.elapsed_time}')
    print(f'count: {measurement.count}')


@profile
def use_iter_optimized():
    measurement = Measurement()

    context = lxml.etree.iterparse('SwissProt.xml', events=('end',), tag='Entry')
    fast_iter(context, measurement.increment_count)

    print(f'elapsed_time(use_iter_optimized): {measurement.elapsed_time}')
    print(f'count: {measurement.count}')


def fast_iter(context, func):
    for event, elem in context:
        func(elem)
        elem.clear()
        while elem.getprevious() is not None:
            del elem.getparent()[0]
    del context


if __name__ == '__main__':
    if sys.argv[1] == '1':
        use_parse()

    if sys.argv[1] == '2':
        use_iter()

    if sys.argv[1] == '3':
        use_iter_optimized()
