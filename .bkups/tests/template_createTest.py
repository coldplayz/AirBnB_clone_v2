    def test_createState(self):
        ''' Tests the console's `create State` command.
        '''
        storage = console.storage
        # Save number of objects; expected value == 0
        before = storage.all()
        lenBefore = len(before)

        # Issue console command
        with patch('sys.stdout', new=StringIO()) as f:
            interpreter.onecmd('create State name="Lagos"')

        # Fetch objects from previously empty storage
        storage.reload()
        after = storage.all()
        lenAfter = len(after)

        # TEST for new object actually created
        self.assertEqual(lenAfter - lenBefore, 1)

        for key in after:
            state = after[key]
            # TEST for correct type of attributes
            self.assertIs(type(state.name), str)
