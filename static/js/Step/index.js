var React = require('react');
var Basic = require('./types/Basic');




var style = {
    main: {
        display: 'block',
        flexWrap: 'wrap',
        fontFamily: '"Helvetica Neue", Helvetica, Arial',
        fontWeight: 800,
        color: '#f3f3f3'
    }
};

class Steps extends React.Component {
    render() {
        const {flat, type} = this.props;
        const items = this.props.items.map((item, idx, list) => {
            return <Basic key={idx} item={item} flat={flat} idx={idx}/>;
        });

        return (
            <div style={style.main}>
                {items}
            </div>
        );
    }
}

export default Steps;
