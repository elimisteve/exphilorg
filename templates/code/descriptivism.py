import exphil
import exphil.objects.query

class Descriptivism(exphil.Theory):

    def __init__(self):

        self.exphil_attrs.update({
            'theory_type': ['reference', 'names'],
        })


    def refers_to(self, ref):
        '''
        Answers the question, "what does `ref` refer to (according to
        Descriptivism)?"

        TODO(sdp): Decide which `ref` types should be accepted.  (Just
        dicts? Strings? Some types should refer to themselves,
        perhaps.)
        '''
        if ref is None:
            return None

        # Make sure we have a dict, or something dict-like
        if not isinstance(ref, dict):
            ref = ref.__dict__

        objs = exphil.objects.query.by_dict(ref)

        if isinstance(objs, dict):
            return objs

        # Descriptivism demands that descriptions be definite; they
        # may not be ambiguous/refer to multiple things
        if len(objs) > 1:
            raise ValueError(
                "Reference is ambiguous; refers to {} objects: {}".format(
                    len(objs), objs
                )
            )

        if not objs:
            return None

        # Turns objs into list in case it's a set, so we can grab the
        # 0th element
        return list(objs)[0]


    def refers(self, ref):
        return self.refers_to(ref) != None


descriptivism = Descriptivism()

if __name__ == '__main__':
    from exphil.objects import people

    nietzsche = {
        'last_name':   'Nietzsche',
        'author_of':   'Thus Spake Zarathustra',
        'philosopher': True,
        'mustache':    True,
    }

    entities = [people.SantaClaus, {'king': True}, {'first_name': 'Santa'}, nietzsche]

    print "According to Descriptivism:\n"
    for entity in entities:
        print "{}\n    refers to\n{}\n".format(entity, descriptivism.refers_to(entity))
