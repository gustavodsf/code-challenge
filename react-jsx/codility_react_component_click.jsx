
import cx from 'classnames';
import { Component } from 'react';

export default class Counter extends  Component {
    constructor(props) {
        super(props);
        this.state = {counter: 42};
    }

    incrementCounter = () => {
        this.setState(prevState => ({counter: prevState.counter + 1}))
    }

    render() {
        return (
            <>
                <div>
                    <h2 className="counter">{this.state.counter}</h2>
                    <button  className="counter-button" onClick={this.incrementCounter}>
                        Click
                    </button>
                </div>
                <style>{`
                    .counter-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                `}</style>
            </>
        );
    }
}
