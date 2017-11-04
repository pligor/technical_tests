package pligor;

import burlap.behavior.singleagent.auxiliary.performance.LearningAlgorithmExperimenter;
import burlap.behavior.singleagent.auxiliary.performance.PerformanceMetric;
import burlap.behavior.singleagent.auxiliary.performance.TrialMode;
import burlap.behavior.singleagent.learning.LearningAgent;
import burlap.behavior.singleagent.learning.LearningAgentFactory;
import burlap.behavior.singleagent.learning.tdmethods.QLearning;
import burlap.domain.singleagent.gridworld.GridWorldDomain;
import burlap.domain.singleagent.gridworld.GridWorldTerminalFunction;
import burlap.domain.singleagent.gridworld.GridWorldVisualizer;
import burlap.domain.singleagent.gridworld.state.GridAgent;
import burlap.domain.singleagent.gridworld.state.GridLocation;
import burlap.domain.singleagent.gridworld.state.GridWorldState;
import burlap.mdp.auxiliary.common.ConstantStateGenerator;
import burlap.mdp.auxiliary.common.SinglePFTF;
import burlap.mdp.auxiliary.stateconditiontest.TFGoalCondition;
import burlap.mdp.core.TerminalFunction;
import burlap.mdp.core.oo.propositional.PropositionalFunction;
import burlap.mdp.core.state.State;
import burlap.mdp.singleagent.SADomain;
import burlap.mdp.singleagent.common.GoalBasedRF;
import burlap.mdp.singleagent.environment.SimulatedEnvironment;
import burlap.mdp.singleagent.model.RewardFunction;
import burlap.mdp.singleagent.oo.OOSADomain;
import burlap.shell.visual.VisualExplorer;
import burlap.statehashing.simple.SimpleHashableStateFactory;
import burlap.visualizer.Visualizer;


public class SolveMazeGridWorld {

    public static void main(String[] args) {

        GridWorldDomain gw = new GridWorldDomain(5, 5);

        int[][] mymap = {
                //rotated 90degrees clockwise from what you see in python
                {0, 0, 0, 0, 0},
                {0, 0, 1, 1, 0},
                {1, 1, 1, 1, 0},
                {0, 0, 1, 0, 0},
                {0, 0, 0, 0, 1}
        };

        gw.setMap(mymap);

        //gw.setMapToFourRooms(); //four rooms layout
        gw.setProbSucceedTransitionDynamics(0.8); //stochastic transitions with 0.8 success rate

        //setup initial state
        State s = new GridWorldState(new GridAgent(0, 2), new GridLocation(4, 2, "loc0"));

        final TerminalFunction tf = new SinglePFTF(
                PropositionalFunction.findPF(gw.generatePfs(), GridWorldDomain.PF_AT_LOCATION));
        //TODO final TerminalFunction tf = new GridWorldTerminalFunction(4,2);;

        //reward function definition
        //big reward if the
        final RewardFunction rf = new GoalBasedRF(new TFGoalCondition(tf), 10., -0.05);
        //TODO change the reward function to be more bad near the beginning and better near final destination

        gw.setTf(tf);
        gw.setRf(rf);

        final OOSADomain domain = gw.generateDomain(); //generate the grid world domain

        //initial state generator
        final ConstantStateGenerator sg = new ConstantStateGenerator(s);

        //set up the state hashing system for looking up states
        final SimpleHashableStateFactory hashingFactory = new SimpleHashableStateFactory();

        //Create factory for Q-learning agent
        LearningAgentFactory qLearningFactory = new LearningAgentFactory() {

            public String getAgentName() {
                return "Q-learning";
            }

            public LearningAgent generateAgent() {
                return new QLearning(domain, 0.99, hashingFactory, 0.3, 0.1);
            }
        };


        //define learning environment
        SimulatedEnvironment env = new SimulatedEnvironment(domain, sg);

        //define experiment
        LearningAlgorithmExperimenter exp = new LearningAlgorithmExperimenter(env,
                10, 1000, qLearningFactory);

        exp.setUpPlottingConfiguration(500, 250, 2, 1000,
                TrialMode.MOST_RECENT_AND_AVERAGE,
                //PerformanceMetric.CUMULATIVE_STEPS_PER_EPISODE,
                PerformanceMetric.AVERAGE_EPISODE_REWARD);

        //start experiment
        exp.startExperiment();

        /*//create visualizer and explorer
        Visualizer v = GridWorldVisualizer.getVisualizer(gw.getMap());
        VisualExplorer exp = new VisualExplorer(domain, v, s);

        //set control keys to use w-s-a-d
        exp.addKeyAction("w", GridWorldDomain.ACTION_NORTH, "");
        exp.addKeyAction("s", GridWorldDomain.ACTION_SOUTH, "");
        exp.addKeyAction("a", GridWorldDomain.ACTION_WEST, "");
        exp.addKeyAction("d", GridWorldDomain.ACTION_EAST, "");

        exp.initGUI();*/

    }

}
