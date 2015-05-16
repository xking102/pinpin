var React = require('react');
var Router = require('react-router');
var { Route, DefaultRoute, RouteHandler, Link } = Router;
var data = require('./data');

var CategoryNav = React.createClass({
  getInitialState: function () {
    return { isOpen: this.props.defaultIsOpen};
  },

  getDefaultProps: function () {
    return { isOpen: false };
  },

  componentWillReceiveProps: function (newProps) {
    if (!this.state.isOpen)
      this.setState({ isOpen: newProps.defaultIsOpen });
  },

  toggle: function () {
    this.setState({ isOpen: !this.state.isOpen });
  },

  buildToggleClassName: function () {
    var toggleClassName = 'CategoryNav__Toggle';
    if (this.state.isOpen)
      toggleClassName += ' CategoryNav__Toggle--is-open';
    return toggleClassName;
  },

  renderItems: function () {
    var category = this.props.category;
    return this.state.isOpen ? category.items.map(function (item) {
      var params = { name: item.name, category: category.name };
      return (
        <li key={item.name}>
          <Link to="item" params={params}>{item.name}</Link>
        </li>
      );
    }) : null;
  },


  render: function () {
    var category = this.props.category;
    return (
      <div className="CategoryNav">
        <h3
          className={this.buildToggleClassName()}
          onClick={this.toggle}
        >{category.name}</h3>
        <ul>{this.renderItems()}</ul>  
      </div>
    );
  }
});

var Sidebar = React.createClass({
  renderCategory: function (category) {
    return <CategoryNav
      key={category.name}
      defaultIsOpen={category.name === this.props.activeCategory}
      category={category}
    />;
  },

  render: function () {
    return (
      <div className="Sidebar">
        {this.props.categories.map(this.renderCategory)}
      </div>
    );
  }
});

var App = React.createClass({

  contextTypes: {
    router: React.PropTypes.func.isRequired
  },

  render: function () {
    var activeCategory = this.context.router.getCurrentParams().category;
    console.log(activeCategory);
    return (
      <div>
        <Sidebar activeCategory={activeCategory} categories={data.getAll()}/>
        <div className="Content">
          <RouteHandler/>
        </div>
      </div>
    );
  }
});

var Item = React.createClass({

  contextTypes: {
    router: React.PropTypes.func.isRequired
  },

  render: function () {
    var params = this.context.router.getCurrentParams();
    var category = data.lookupCategory(params.category);
    var item = data.lookupItem(params.category, params.name);
    return (
      <div>
        <h2>{category.name} / {item.name}</h2>
        <p>Price: ${item.price}</p>
      </div>
    );
  }
});

var Index = React.createClass({
  render: function () {
    return (
      <div>
        
      </div>
    );
  }
});

var routes = (
  <Route handler={App}>
    <DefaultRoute handler={Index}/>
    <Route name="item" path=":category/:name" handler={Item} />
  </Route>
);

Router.run(routes, function (Handler) {
  React.render(<Handler/>, document.getElementById('app'));
});
