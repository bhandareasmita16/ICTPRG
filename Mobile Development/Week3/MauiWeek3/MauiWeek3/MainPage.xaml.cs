namespace MauiWeek3;

public partial class MainPage : ContentPage
{
	int count = 0;

	public MainPage()
	{
		//DO NOT PUT ANYTHING HERE THAT INTERACTS WITH THE UI
		//UI NOT BUILT
		InitializeComponent(); //Builds the UI from XAML

	}

/*	private void OnCounterClicked(object sender, EventArgs e)
	{
		count++; //Unary
		++count;

		if (count == 1)
			CounterBtn.Text = $"Clicked {count} time";
		else
			CounterBtn.Text = $"Clicked {count} times";

		SemanticScreenReader.Announce(CounterBtn.Text);
	}*/
}

