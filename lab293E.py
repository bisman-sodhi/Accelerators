import pyrtl

def c_conjecture(n, bitwidth):
    num = pyrtl.Register(bitwidth, 'num')
    i = pyrtl.Register(bitwidth, 'i')
    done = pyrtl.WireVector(bitwidth=1, name='done')
    state = pyrtl.Register(bitwidth=1, name='state')
    with pyrtl.conditional_assignment:
        with state:
            with num != 0x1:
                with num[0] == 0:
                    num.next |= pyrtl.corecircuits.shift_right_logical(num, pyrtl.Const(1))
                    i.next |= i + 0x1
                with num[0] != 0:
                    num.next |= ((pyrtl.corecircuits.shift_left_logical(num, pyrtl.Const(1)) + num) + pyrtl.Const(1))
                    i.next |= i + 0x1
            with num == 0x1:
                i.next |= 0
        with ~state:
            state.next |= 1
            num.next |= n
    done <<= num == 1
    return num, i, done


BITWIDTH = 8

N = pyrtl.Input(BITWIDTH, 'N')
N_out = pyrtl.Output(BITWIDTH, 'N_out')
iter_out = pyrtl.Output(BITWIDTH, 'iter_out')
done_out = pyrtl.Output(1, 'done_out')

output = c_conjecture(N,len(N))
N_out <<= output[0]
iter_out <<= output[1]
done_out <<= output[2]

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

#sim.step({'N': 12})
while not (sim.inspect('done_out')):
    sim.step({'N': 10})

sim_trace.render_trace(trace_list=['N', 'N_out', 'iter_out', 'done_out'])
