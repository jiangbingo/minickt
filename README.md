minickt
=======

Analyzer and simulator of logic circuit

---

### Environments

You have to install `Python2` (python2.7.6 is the version in development).<br />
And you do not need to install minickt, it's just a script.

If you want to use the complete functions of minickt, you should install python packages: `matplotlib` and `networkx`.

---

### Run minickt

```sh
$ python minickt.py 
```

and you can run any avalible command by enter it after the prompt `[ miniCkt ] >> `:

```
[ miniCkt ] >> exit
```

Command `exit` will terminate minickt.

---

### List commands and get help

Use "?" to list all avalible commands in minickt.

```
[ miniCkt ] >> ?

Documented commands (type help <topic>):
========================================
cc       encode        help       ls_writer  sat         shell     
chname   eval          loadsc     read       sat_reason  show      
cmd      exit          ls         reason     sec         show_ckt  
collect  gen_cone_ckt  ls_ckt     reset      set         show_ratio
cone     get           ls_parser  rm         sg          write
```

or use "cmd" to get the short description of all commands

```
[ miniCkt ] >> cmd
```

If you want to know the details of a specified cmd, use `help<cmd>` or `?<cmd>`:

```
[ miniCkt ] >> ?shell
[ miniCkt ] >> help shell
```

---

### Circuit I/O

Let me introduce you the commands of circuit IO.

#### Read a logic circuit

Command `read` can read a logic circuit with specified parser.

```
[ miniCkt ] >> read mycircuit.v by primitive
read mycircuit.v ...
success: circuit "top(mycircuit.v) is in circuit manager now
```

Commmand `ls -p` or `ls_parser` can list all avalible parsers.<br />
You can write parser by yourself to fit the circuit format.

#### Rename

The default name of a circuit is `top(CIRCUIT_FILE_NAME)`.<br />
You can use `chname` to rename it.

```
[ minickt ] >> chname ckt1
```

Now we can use cmd `ls -c` or `ls_ckt` to list all circuits in circuit manager of minickt.

```
[ miniCkt ] >> ls -c
there are 1 circuits now
[0] ckt1 <--- current
```

It means that minickt can hold several circuits not just single one! <br />
I will talk about this later.

#### Write out a circuit

use `write` to write out the circuit.

```
[ miniCkt ] >> write ckt1.v by primitive
```

The format of `write` is similar to `read`.<br />
Commmand `ls -w` or `ls_writer` can list all avalible writers.<br />
You can write your own writer, too.

---

### Circuit Analysis

Here are some methods of doing analyzing

#### Get circuit infomation

Command `get` can get the specified property of circuit.

```
[ miniCkt ] >> get gate_num
```

try `?get` to know the properies that can be acquired by `get`.

#### Show graph

`show_ckt` or `show -c`  will show a circuit graph by taking each logic gate as a node.<br />
`show_ratio` or `show -r` will show a pie chart of gates ratio.

---

### Circuit Simulation

This part will introduct the method to set the gate values and doing simulation.

#### List gates and their infomation

`sg` can list a gate or a gate set in current circuit.<br />
For example, if you want to see all of the gates in ciruict:

```
[ miniCkt ] >> sg all
```

Or you want to see the PI gate:

```
[ miniCkt ] >> sg pi
```

Or you just want to see the PO gate named po_0:

```
[ miniCkt] >> sg po_0
```

Even you can mix them:

```
[ miniCkt ] >> sg pi, po_0
```

We could add some additional options to see more information.

```
[ miniCkt ] >> sg pi -ivo
```

`-i` will list the fanins of each gate.<br />
`-o` will list the fanouts of each gate.<br />
`-v` will list the values of each gates.


#### Set gate value

You can assign value to a "gate" or a "gate set".<br />
For example, we want to assign one(True) to all PI gates:

```
[ miniCkt ] >> set pi 1
```

If you want to reset all gates(it means you want to let all gates value be unknown):

```
[ miniCkt ] >> reset
```

#### Simulation

After setting the gate values of circuit, we can do simulation with cmd `eval` which means evaluate:

```
[ miniCkt ] >> eval
```

We commonly use `sg -v` to check the evalation results.

---

### Circuit Reasoning

minickt also supports circuit reasoning. <br />
There are two ways to do that: cmd `reason` and `sat_reason`.

After doing assignments to some gates , we can use `reason` to deduce other gates' values:

```
[ miniCkt ] >> reset
[ miniCkt ] >> set po 1
[ miniCkt ] >> reason
```

If some conflict occur, reasoning will fail.<br />
Note that this command just deduces the values which can be implied directly, it does not do any guess.

If you want to do a complete reasoning, use `sat_reason`:

```
[ miniCkt ] >> sat_reason po_0 1
```

User should be ware of the differences between `read` and `sat_reason`.<br />
`sat_reason` does not depend on the current assignments, it depends on gates and their values specified with command.

Also, this command use an external SAT solver which is located in directory `bin` with name `lingeling`.<br />
You should check the name and the version fo SAT solver are avalible, otherwise it will result in fail.

---

### Circuit Manager

You could add several circuits to minickt because it can hold multiple circuits.(I think it's really cool!)

#### Circuit switching

Assume we have two circuits in circuit manager(the current arrow points the "current circuit"):

```
[ miniCkt ] >> ls -c
there are 2 circuits now
[0] ckt1 <--- current
[1] ckt2
```

Current circuit is the circuit which can be controled directly by commands.

User can use `cc` to switch to the circuit we want to control and do something.

```
[ miniCkt ] >> cc 1
[ miniCkt ] >> ls -c
there are 2 circuits now
[0] ckt1
[1] ckt2 <--- current
```

#### Remove circuit

`rm` can remove the current circuit(if no option) or remove the i-th circuit.

```
[ miniCkt ] >> rm
[ miniCkt ] >> rm 0
```

#### Get cone circuit

You can specify a gate to get its `cone` circuit.

```
[ miniCkt ] >> cone po_0
```

It generates a new circuit with default name "coneckt"(it can be specified).

But sometimes we want an independent cone circuit, we can do by:

```
[ miniCkt ] >> cone po_0
[ miniCkt ] >> write ckt1.v by primitive
[ miniCkt ] >> rm
[ miniCkt ] >> read ckt1.v by primitive
```

or use a combinational command `gen_cone_ckt` which is eqaul to the commands above.

```
[ miniCkt ] >> gen_cone_ckt po_0
```

---

### Verification

minickt also supports some functions of verification.

#### Circuit SAT

---

### minickt Script

---

### Shell commands

---





